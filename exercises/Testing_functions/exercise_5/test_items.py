import unittest
from Items import find_item

class ItemsTestCase(unittest.TestCase):
    def test_find_item_function(self):
        result = find_item('banana', ['orange', 'banana', 'apple'])
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()