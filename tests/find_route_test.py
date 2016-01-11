import unittest
import server

class TestFindRoute(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()
        
    def test_find_route(self):
        response = self.app.get('/find')
        print(response)


if __name__ == '__main__':
    unittest.main()
