import unittest
from main import get_wufoo_data

class MyTestCase(unittest.TestCase):
    def test_something(self):
        response = get_wufoo_data()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 10)


if __name__ == '__main__':
    unittest.main()