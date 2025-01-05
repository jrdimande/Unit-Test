import unittest
from city_function import get_formatted_city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = get_formatted_city_country('maputo', 'mozambique', 33_000_000_000)
        self.assertEqual(formatted, 'Maputo, Mozambique - population 33000000000')


if __name__ == '__main__':
    unittest.main()