import os
import io
import hashlib
import unittest
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, "saas_cloud"))

import app

class MultiChunkTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config["TESTING"] = True
        self.client = app.app.test_client()

    def test_multichunk_upload_and_reassembly(self):
        """Test multi-chunk upload (> 2 MiB, 3 chunks) and reassembly order."""
        total_size = 5 * 1024 * 1024  # 5 MiB
        pattern = b"CHUNKING_VERIFICATION_BLOCK_2026_ANTIGRAVITY\n"
        reps = (total_size // len(pattern)) + 1
        payload = (pattern * reps)[:total_size]
        payload_hash = hashlib.sha256(payload).hexdigest()

        # Upload
        data = {"file": (io.BytesIO(payload), "dataset_5mb.bin")}
        res = self.client.post("/upload", data=data, content_type="multipart/form-data", follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        # Inspect chunks in metadata
        meta = app.load_metadata()
        file_entry = next((v for v in meta.values() if v["filename"] == "dataset_5mb.bin"), None)
        self.assertIsNotNone(file_entry)
        self.assertEqual(file_entry["chunk_count"], 3)
        self.assertEqual(len(file_entry["chunks"]), 3)

        # Verify sequential ordering
        for idx, chunk in enumerate(file_entry["chunks"]):
            self.assertEqual(chunk["index"], idx)

        # Download & verify byte-exact reassembly
        dl_res = self.client.get(f"/download/{file_entry['file_id']}")
        self.assertEqual(dl_res.status_code, 200)
        self.assertEqual(len(dl_res.data), total_size)
        self.assertEqual(hashlib.sha256(dl_res.data).hexdigest(), payload_hash)

        # Cleanup
        self.client.post(f"/delete/{file_entry['file_id']}", follow_redirects=True)

if __name__ == "__main__":
    unittest.main()
