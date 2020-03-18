'''
Authors: Almog Mahluf - 205490170
         Alon Gabay   - 2080646080
         Michael Elisha -
'''
import unittest
from unittest.mock import Mock, patch
from src.geo_class import Geo


class MyTestCase(unittest.TestCase):
    '''
    This Class tests Geo's class functions.
    '''

    @patch('src.geo_class.requests.get')
    def test_valid_ip_in_valid_range(self, mock_get):
        '''
        Tests the case when the ip is valid and it is in the range of valids.
        :param mock_get: The mock of the IP-API json functionality of this method
        :return:
        '''
        ip_information = {'status': 'success',
                          'country': 'United States',
                          'countryCode': 'US',
                          'region': 'NJ',
                          'regionName': 'New Jersey',
                          'city': 'Newark',
                          'zip': '07175',
                          'lat': 40.7357,
                          'lon': -74.1724,
                          'timezone': 'America/New_York',
                          'isp': 'Google LLC',
                          'org': 'Level 3',
                          'as': 'AS15169 Google LLC',
                          'query': '8.8.8.8'}
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = ip_information

        # assume
        stub = '8.8.8.8'

        # expected
        expected = ('US')

        # action
        result = Geo.ip_details(stub)

        # assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
