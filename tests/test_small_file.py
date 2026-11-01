import os
import io
import hashlib
import unittest
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, "saas_cloud"))

import app

class SmallFileRoundtripTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config["TESTING"] = True
        self.client = app.app.test_client()

    def test_small_file_roundtrip(self):
        """Test small-file upload/download round trip (< 2 MiB single chunk)."""
        payload = b"Secure Cloud Vault HDFS single-chunk round-trip payload verification." * 100
        payload_hash = hashlib.sha256(payload).hexdigest()

        # Upload
        data = {"file": (io.BytesIO(payload), "test_doc.txt")}
        res = self.client.post("/upload", data=data, content_type="multipart/form-data", follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        # Retrieve file_id
        meta = app.load_metadata()
        file_entry = next((v for v in meta.values() if v["filename"] == "test_doc.txt"), None)
        self.assertIsNotNone(file_entry)
        self.assertEqual(file_entry["chunk_count"], 1)

        # Download & verify integrity
        dl_res = self.client.get(f"/download/{file_entry['file_id']}")
        self.assertEqual(dl_res.status_code, 200)
        self.assertEqual(hashlib.sha256(dl_res.data).hexdigest(), payload_hash)

        # Cleanup
        self.client.post(f"/delete/{file_entry['file_id']}", follow_redirects=True)

if __name__ == "__main__":
    unittest.main()
