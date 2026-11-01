import os
import io
import json
import uuid
import secrets
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import hdfs

app = Flask(__name__)

# --- Configuration & Environment Variables ---
SAAS_DATA_DIR = os.environ.get("SAAS_DATA_DIR", os.path.dirname(os.path.abspath(__file__)))
os.makedirs(SAAS_DATA_DIR, exist_ok=True)

HDFS_URL = os.environ.get("HDFS_URL", "http://localhost:9870")
HDFS_USER = os.environ.get("HDFS_USER", "vinay_umesh_gole")
HDFS_BASE_DIR = os.environ.get("HDFS_BASE_DIR", "/saas_cloud")
MAX_UPLOAD_BYTES = int(os.environ.get("MAX_UPLOAD_BYTES", 100 * 1024 * 1024))  # 100 MiB
CHUNK_SIZE = 2 * 1024 * 1024  # 2 MiB chunks

app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_BYTES

# --- Secret Keys Setup ---
FLASK_SECRET_KEY_PATH = os.path.join(SAAS_DATA_DIR, "flask-secret.key")
if not os.path.exists(FLASK_SECRET_KEY_PATH):
    with open(FLASK_SECRET_KEY_PATH, "w") as f:
        f.write(secrets.token_hex(32))

with open(FLASK_SECRET_KEY_PATH, "r") as f:
    app.secret_key = f.read().strip()

ENCRYPTION_KEY_PATH = os.path.join(SAAS_DATA_DIR, "secret.key")
if not os.path.exists(ENCRYPTION_KEY_PATH):
    with open(ENCRYPTION_KEY_PATH, "wb") as f:
        f.write(Fernet.generate_key())

with open(ENCRYPTION_KEY_PATH, "rb") as f:
    FERNET_KEY = f.read().strip()
    cipher = Fernet(FERNET_KEY)

# --- Metadata Storage ---
METADATA_FILE = os.path.join(SAAS_DATA_DIR, "files.json")

def load_metadata():
    if not os.path.exists(METADATA_FILE):
        return {}
    try:
        with open(METADATA_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

def save_metadata(data):
    with open(METADATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_hdfs_client():
    """Initializes and returns an InsecureClient to WebHDFS."""
    return hdfs.InsecureClient(HDFS_URL, user=HDFS_USER)

def check_hdfs_health():
    """Verifies WebHDFS connection and base directory."""
    try:
        client = get_hdfs_client()
        status = client.status(HDFS_BASE_DIR, strict=False)
        if status is None:
            client.makedirs(HDFS_BASE_DIR, permission=777)
            status = client.status(HDFS_BASE_DIR)
        return True, "Online", status
    except Exception as e:
        return False, str(e), None

# --- Routes ---

@app.route("/")
def index():
    files_meta = load_metadata()
    hdfs_ok, hdfs_status_msg, hdfs_dir_info = check_hdfs_health()

    total_files = len(files_meta)
    total_raw_bytes = sum(f.get("size", 0) for f in files_meta.values())
    total_chunks = sum(f.get("chunk_count", 0) for f in files_meta.values())

    return render_template(
        "index.html",
        files=files_meta,
        total_files=total_files,
        total_raw_bytes=total_raw_bytes,
        total_chunks=total_chunks,
        hdfs_ok=hdfs_ok,
        hdfs_status_msg=hdfs_status_msg,
        hdfs_url=HDFS_URL,
        hdfs_user=HDFS_USER,
        chunk_size_mb=CHUNK_SIZE // (1024 * 1024),
    )

@app.route("/api/health")
def api_health():
    hdfs_ok, hdfs_status_msg, status_info = check_hdfs_health()
    return jsonify({
        "hdfs_connected": hdfs_ok,
        "hdfs_url": HDFS_URL,
        "hdfs_user": HDFS_USER,
        "status_message": hdfs_status_msg,
        "hdfs_directory_status": status_info,
    })

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        flash("No file part provided in request.", "danger")
        return redirect(url_for("index"))

    uploaded_file = request.files["file"]
    if uploaded_file.filename == "":
        flash("No file selected.", "warning")
        return redirect(url_for("index"))

    safe_name = secure_filename(uploaded_file.filename) or "unnamed_file"
    file_id = str(uuid.uuid4())
    hdfs_file_dir = f"{HDFS_BASE_DIR}/{file_id}"

    try:
        client = get_hdfs_client()
        client.makedirs(hdfs_file_dir, permission=777)

        chunks_meta = []
        chunk_index = 0
        total_bytes = 0

        while True:
            chunk = uploaded_file.read(CHUNK_SIZE)
            if not chunk:
                break

            total_bytes += len(chunk)
            # Encrypt 2 MiB chunk with Fernet
            encrypted_chunk = cipher.encrypt(chunk)
            chunk_path = f"{hdfs_file_dir}/chunk_{chunk_index}.enc"

            # Write chunk to HDFS
            client.write(chunk_path, data=encrypted_chunk, overwrite=True)

            chunks_meta.append({
                "index": chunk_index,
                "raw_size": len(chunk),
                "enc_size": len(encrypted_chunk),
                "hdfs_path": chunk_path,
            })
            chunk_index += 1

        if chunk_index == 0:
            # Handle empty file
            encrypted_chunk = cipher.encrypt(b"")
            chunk_path = f"{hdfs_file_dir}/chunk_0.enc"
            client.write(chunk_path, data=encrypted_chunk, overwrite=True)
            chunks_meta.append({
                "index": 0,
                "raw_size": 0,
                "enc_size": len(encrypted_chunk),
                "hdfs_path": chunk_path,
            })
            chunk_index = 1

        # Record file metadata
        metadata = load_metadata()
        metadata[file_id] = {
            "file_id": file_id,
            "filename": safe_name,
            "size": total_bytes,
            "chunk_count": chunk_index,
            "chunks": chunks_meta,
            "uploaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "hdfs_dir": hdfs_file_dir,
        }
        save_metadata(metadata)

        flash(
            f"Successfully encrypted and split '{safe_name}' ({total_bytes} bytes) into {chunk_index} chunk(s) on HDFS!",
            "success",
        )
    except Exception as e:
        flash(f"Upload failed: {str(e)}", "danger")

    return redirect(url_for("index"))

@app.route("/download/<file_id>")
def download(file_id):
    metadata = load_metadata()
    if file_id not in metadata:
        flash("File metadata not found.", "danger")
        return redirect(url_for("index"))

    file_info = metadata[file_id]
    try:
        client = get_hdfs_client()
        buffer = io.BytesIO()

        # Download and decrypt chunks sequentially
        for chunk in file_info["chunks"]:
            chunk_path = chunk["hdfs_path"]
            with client.read(chunk_path) as reader:
                enc_data = reader.read()
            dec_data = cipher.decrypt(enc_data)
            buffer.write(dec_data)

        buffer.seek(0)
        return send_file(
            buffer,
            as_attachment=True,
            download_name=file_info["filename"],
        )
    except Exception as e:
        flash(f"Download and decryption failed: {str(e)}", "danger")
        return redirect(url_for("index"))

@app.route("/delete/<file_id>", methods=["POST"])
def delete_file(file_id):
    metadata = load_metadata()
    if file_id not in metadata:
        flash("File not found in registry.", "warning")
        return redirect(url_for("index"))

    file_info = metadata[file_id]
    try:
        client = get_hdfs_client()
        client.delete(file_info["hdfs_dir"], recursive=True)
        del metadata[file_id]
        save_metadata(metadata)
        flash(f"File '{file_info['filename']}' and its encrypted chunks were purged from HDFS.", "info")
    except Exception as e:
        flash(f"Error deleting chunks from HDFS: {str(e)}", "danger")

    return redirect(url_for("index"))

@app.route("/api/file/<file_id>")
def file_details(file_id):
    metadata = load_metadata()
    if file_id not in metadata:
        return jsonify({"error": "File not found"}), 404
    return jsonify(metadata[file_id])

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 5000))
    app.run(host=host, port=port, debug=False)
