import unittest
import pprint

from street_parking.signs_finder import get_signs, get_grouped_signs

class TestSignsFinder(unittest.TestCase):

    def test_get_signs_from_lat_long(self):
        signs = get_signs('40.7135097', '-73.9859414', 100) 
        self.assertEqual(len(signs), 75)

    def test_get_signs_grouping_same_signs(self):
        signs = get_grouped_signs('40.7135097', '-73.9859414', 100)
        self.assertEqual(len(signs), 57)
        
if __name__ == '__main__':
    unittest.main()
