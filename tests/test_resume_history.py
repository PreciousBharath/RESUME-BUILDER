import os
import tempfile
import unittest

import app as app_module


class ResumeHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_base_dir = app_module.BASE_DIR
        self.original_upload_folder = app_module.UPLOAD_FOLDER
        self.original_users_file = app_module.USERS_FILE
        self.original_resumes_file = getattr(app_module, "RESUMES_FILE", None)

        app_module.BASE_DIR = self.temp_dir.name
        app_module.UPLOAD_FOLDER = os.path.join(self.temp_dir.name, "uploads")
        app_module.USERS_FILE = os.path.join(self.temp_dir.name, "users.json")
        app_module.RESUMES_FILE = os.path.join(self.temp_dir.name, "resumes.json")
        os.makedirs(app_module.UPLOAD_FOLDER, exist_ok=True)
        app_module.ensure_users_file()

    def tearDown(self):
        app_module.BASE_DIR = self.original_base_dir
        app_module.UPLOAD_FOLDER = self.original_upload_folder
        app_module.USERS_FILE = self.original_users_file
        if self.original_resumes_file is not None:
            app_module.RESUMES_FILE = self.original_resumes_file
        self.temp_dir.cleanup()

    def test_save_and_load_resume_history(self):
        record = app_module.save_resume_record(
            user_email="ada@example.com",
            data={
                "name": "Ada Lovelace",
                "email": "ada@example.com",
                "phone": "123456",
                "role": "Developer",
                "summary": "Great engineer",
                "skills": "Python",
                "education": "University",
                "experience": "Built apps",
                "photo": None,
                "template": 2,
                "accent_color": "purple",
                "format": "pdf",
            },
            file_path="/tmp/resume.pdf",
            download_name="ada_resume.pdf",
        )

        history = app_module.load_resume_history("ada@example.com")

        self.assertEqual(1, len(history))
        self.assertEqual(record["id"], history[0]["id"])
        self.assertEqual("Ada Lovelace", history[0]["name"])
        self.assertEqual("pdf", history[0]["format"])


if __name__ == "__main__":
    unittest.main()
