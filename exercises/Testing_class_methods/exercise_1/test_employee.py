import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_give_default_raise(self):
        employee = Employee('michael', 'jackson', 10_000)
        employee.give_raise()
        self.assertEqual(employee.annual_salary, 15_000)

    def test_give_custom_raise(self):
        pass


if __name__ == '__main__':
    unittest.main()