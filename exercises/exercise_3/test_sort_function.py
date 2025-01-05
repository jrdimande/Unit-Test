import unittest
from sort_function import sort_n

class SortTestCase(unittest.TestCase):

    def test_sort(self):
        result = sort_n([1, 4, 3, 7, 2, 9,5])
        self.assertEqual(result, [1, 2, 3, 4, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()