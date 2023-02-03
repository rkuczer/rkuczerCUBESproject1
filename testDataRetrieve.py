import unittest
from main import get_wufoo_data

class MyTestCase(unittest.TestCase):
    def test_data_num(self):
        response = get_wufoo_data()
        data1 = response['Entries']
        self.assertEqual(10,len(data1))

    def


if __name__ == '__main__':
    unittest.main()