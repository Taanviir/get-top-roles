import unittest
from app import app


class TestGetTopRolesAPI(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.client = app.test_client()
        self.base_url = "/get-top-roles"

    def test_valid_student_id(self):
        # Test with a valid student ID
        response = self.client.get(f"{self.base_url}?student_id=1")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["student_name"], "Alice")
        self.assertEqual(len(data["top_roles"]), 5)
        self.assertIn("Developer", data["top_roles"])

    def test_valid_student_id_2(self):
        # Test with another valid student ID
        response = self.client.get(f"{self.base_url}?student_id=2")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["student_name"], "Bob")
        self.assertEqual(len(data["top_roles"]), 5)
        self.assertIn("Marketing Specialist", data["top_roles"])

    def test_missing_student_id(self):
        # Test with no student ID provided
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data["error"], "Missing student_id parameter")

    def test_invalid_student_id(self):
        # Test with a student ID that doesn't exist
        response = self.client.get(f"{self.base_url}?student_id=999")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["error"], "No data found for student: 999")

    def test_student_id_as_non_integer(self):
        # Test with a non-integer student ID
        response = self.client.get(f"{self.base_url}?student_id=abc")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["error"], "No data found for student: abc")


if __name__ == "__main__":
    unittest.main()
