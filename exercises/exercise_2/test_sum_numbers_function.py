import unittest
from sum_numbers_function import sum_numbers

class SumTestCase(unittest.TestCase):
    def test_sum_numbers(self):
        result = sum_numbers([1, 2, 3])
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()