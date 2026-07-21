import unittest

from app import app


class NewPagesTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_toolkit_page_loads(self):
        response = self.client.get('/toolkit')
        self.assertEqual(200, response.status_code)
        self.assertIn('Career Toolkit', response.get_data(as_text=True))

    def test_tips_page_loads(self):
        response = self.client.get('/tips')
        self.assertEqual(200, response.status_code)
        self.assertIn('Resume Tips', response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
