import unittest

from street_parking.signs_finder import get_signs

class TestSignsFinder(unittest.TestCase):

    def test_get_signs_from_lat_long(self):
        signs = get_signs('40.7135097', '-73.9859414', 100) 
        
        print(len(signs))
        self.assertEquals(True, False)


if __name__ == '__main__':
    unittest.main()
