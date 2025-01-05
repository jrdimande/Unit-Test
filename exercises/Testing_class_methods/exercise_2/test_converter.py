import unittest
from converter import UnitConverter

class TestUnitConverter(unittest.TestCase):
    def test_convert_kelvin_to_celcius(self):
        converter = UnitConverter()
        result = converter.convert_kelvin_to_celsius(200)
        self.assertEqual(result, -73.15)

    def test_convert_celcius_to_fahrenheit(self):
        convert = UnitConverter()
        result = convert.convert_celcius_to_fahrenheit(200)
        self.assertEqual(result,399 ) """failing"""

if __name__ == '__main__':
    unittest.main()