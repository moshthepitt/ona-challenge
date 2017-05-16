import unittest

from ona import get_request, get_data, calculate


class TestStringMethods(unittest.TestCase):
    url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

    def test_request(self):
        r = get_request(self.url)
        self.assertEqual(r.status_code, 200)

    def test_data(self):
        data = get_data(self.url)
        self.assertTrue(isinstance(data, list))

    def test_result(self):
        c = calculate(self.url)
        self.assertTrue(isinstance(c['number_functional'], int))
        self.assertTrue(isinstance(c['number_water_points'], list))
        self.assertTrue(isinstance(c['community_ranking'], list))

if __name__ == '__main__':
    unittest.main()
