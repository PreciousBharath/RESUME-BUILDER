import unittest

from app import app


class DashboardStyleTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_dashboard_persists_selected_style(self):
        with self.client.session_transaction() as session:
            session["user"] = {"email": "ada@example.com", "name": "Ada"}

        response = self.client.post(
            "/dashboard",
            data={"template": "3", "accent": "rose"},
            follow_redirects=True,
        )

        self.assertEqual(200, response.status_code)
        with self.client.session_transaction() as session:
            self.assertEqual("3", session["selected_style"]["template"])
            self.assertEqual("rose", session["selected_style"]["accent"])


if __name__ == "__main__":
    unittest.main()
