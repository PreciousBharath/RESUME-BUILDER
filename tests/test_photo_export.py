import os
import shutil
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from create_resume import generate_resume_docx, generate_resume_pdf


class PhotoExportTests(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).resolve().parent.parent
        self.upload_dir = self.project_root / "static" / "uploads"
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.photo_path = self.upload_dir / "test_photo.png"
        Image.new("RGB", (120, 120), color="blue").save(self.photo_path)

    def tearDown(self):
        if self.photo_path.exists():
            self.photo_path.unlink()

    def test_exporters_use_legacy_relative_photo_paths(self):
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "123",
            "role": "Developer",
            "summary": "Summary",
            "skills": "Python",
            "education": "BSc",
            "experience": "2 years",
            "goal": "Grow",
            "linkedin": "",
            "portfolio": "",
            "certifications": "",
            "projects": "",
            "languages": "",
            "achievements": "",
            "photo": "uploads/test_photo.png",
            "template": 1,
            "accent_color": "blue",
            "show_photo": True,
        }

        docx_buffer = generate_resume_docx(data, template=1)
        pdf_buffer = generate_resume_pdf(data, template=1)

        self.assertGreater(len(docx_buffer.getvalue()), 0)
        self.assertGreater(len(pdf_buffer.getvalue()), 0)


if __name__ == "__main__":
    unittest.main()
