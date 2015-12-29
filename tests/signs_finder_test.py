import unittest
import pprint

from street_parking.signs_finder import get_signs

class TestSignsFinder(unittest.TestCase):

    def test_get_signs_from_lat_long(self):
        signs = get_signs('40.7135097', '-73.9859414', 100) 
        pp = pprint.PrettyPrinter(indent=4)
        self.assertEquals(True, False)


if __name__ == '__main__':
    unittest.main()
