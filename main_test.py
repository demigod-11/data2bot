from main import *
from test_data import *
import unittest


class TestMain(unittest.TestCase):

    def test_parse_json(self, filepath = './data/data_1.json'):
        self.assertEqual(type(parse_json(filepath)), dict)

    def test_parse_json_exception(self, filepath = 'unknown/path'):
        with self.assertRaises(Exception):
            parse_json(filepath)
            
    def test_clean_data(self, data = data):
        self.assertEqual(type(clean_data(data)), dict)

    def test_clean_data_exception(self, data = input_data):
        with self.assertRaises(Exception):
            clean_data(data)

    def test_create_schema(self, input_data = input_data, expected = expected):
        self.assertDictEqual(create_schema(input_data), expected)

    def test_write_to_json(self, data = data, file = file):
        self.assertEqual(WritetoJson(data,file), 0)
    
    def test_write_to_json_exception(self, data = data, file = './unknown/path'):
        with self.assertRaises(Exception):
            WritetoJson(data, file)
    

if __name__ == "__main__":
    unittest.main()
