import unittest
import requests


class It_test_rest_api(unittest.TestCase):
    def test_checkendpoint(self):
        data = requests.get("http://127.0.0.1:5000/getquckUnioncodeDC")
        self.assertIsNotNone(data.content)


if __name__ == '__main__':
    unittest.main()

