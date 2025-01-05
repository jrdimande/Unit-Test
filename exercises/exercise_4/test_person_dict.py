import unittest
from person_dict import _dict

class PersonTestCase(unittest.TestCase):
    def test_dict_function(self):
        result = _dict('ian', 12, 'python')
        self.assertEqual(result, {'name' : 'ian', 'age' : 12, 'favorite_language' : 'pyhton'})

if __name__ == '__main__':
    unittest.main()