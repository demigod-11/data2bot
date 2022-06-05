from main import *
import unittest
import os

input = {'name' : "sam",
         'age' : 4,
         'fruits' : ['apple', 'coke'],
         'cousins' : [{'mother': {}, 'father': {}}]
}

expected = {
 'name': {'type': 'string', 'tag': '', 'description': '', 'required': False},
 'age': {'type': 'integer', 'tag': '', 'description': '', 'required': False},
 'fruits': {'type': 'enum', 'tag': '', 'description': '', 'required': False},
 'cousins': {'type': 'array', 'tag': '', 'description': '', 'required': False}
}


class TestMain(unittest.TestCase):
    # all this not running


    # def source_file_exist(self):
    #     self.assertTrue(os.path.isfile("path"))
    
    # def sink_file_exist(self):
    #     self.assertTrue(os.path.isfile("path"))

    # def json_file_not_empty(self):
    #     self.assertTrue(os.stat("path").st_size)

    def test_parse_json(self, filepath):
        self.assertEqual(type(parse_json(filepath)), list)

    def test_parse_json_exception(self, filepath):
        with self.assertRaises(Exception):
            parse_json(filepath)
            
    def test_clean_data(self, data):
        self.assertEqual(type(clean_data(data)), dict)

    def test_clean_data_exception(self, data):
        with self.assertRaises(Exception):
            clean_data(data)

    def test_create_schema(self, input, expected):
        self.assertDictEqual(create_schema(input), expected)

    def test_write_to_json(self, data, file):
        self.assertEqual(WritetoJson(data,file), 0)
    
    def test_write_to_json_exception(self, data, file):
        with self.assertRaises(Exception):
            WritetoJson(data, file)
    

if __name__ == "__main__":
    unittest.main()


