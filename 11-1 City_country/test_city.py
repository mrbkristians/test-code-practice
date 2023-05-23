import unittest
from city_functions import format_city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formated_name = format_city_country('santiago', 'chile')
        self.assertEqual(formated_name, "Santiago, Chile")

    def test_city_country_population(self):
        formated_name = format_city_country('santiago', 'chile', '2000000')
        self.assertEqual(formated_name, "Santiago, Chile - population 2000000")

if __name__ == '__main__':
    unittest.main()