'''
Authors: Almog Mahluf - 205490170
         Alon Gabay   - 2080646080
         Michael Elisha - 316904978
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
        expected = ('US', 'Newark', 'Google LLC', '8.8.8.8')

        # action
        result = Geo.ip_details(stub)

        # assert
        self.assertEqual(result, expected)

    @patch('src.geo_class.requests.get')
    def test_invalid_ip(self, mock_get):
        '''
        Tests the case when the ip is invalid.
        :param mock_get: The mock of the IP-API json functionality of this method
        :return:
        '''
        ip_information = {'status': 'fail',
                          'message': 'invalid query',
                          'query': 'XXX'}
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = ip_information

        # assume
        stub = 'XXX'

        # expected
        expected = None

        # action
        result = Geo.ip_details(stub)

        # assert
        self.assertEqual(result, expected)

    @patch('src.geo_class.requests.get')
    def test_valid_ip_not_valid_range(self, mock_get):
        '''
           Tests the case when the ip is valid and it is not in the range of valids.
           :param mock_get: The mock of the IP-API json functionality of this method
           :return:
        '''
        ip_information = {'status': 'fail',
                          'message': 'private range',
                          'query': '192.168.56.1'}
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = ip_information

        # assume
        stub = '192.168.56.1'

        # expected
        expected = 'private range'

        # action
        result = Geo.ip_details(stub)

        # assert
        self.assertEqual(result, expected)

    @patch('src.geo_class.requests.get')
    def test_valid_status_isp(self, mock_get):
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
        expected = 'Google LLC'

        # action
        result = Geo.ip_isp_name(stub)

        # assert
        self.assertEqual(result, expected)

    @patch('src.geo_class.requests.get')
    def test_invalid_status_isp(self, mock_get):
        '''
           Tests the case when the ip invalid
           :param mock_get: The mock of the IP-API json functionality of this method
           :return:
        '''
        ip_information = {'status': 'fail',
                          'message': 'invalid query',
                          'query': 'XYZ'}
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = ip_information

        # assume
        stub = 'XYZ'

        # expected
        expected = 'fail'

        # action
        result = Geo.ip_isp_name(stub)

        # assert
        self.assertEqual(result, expected)

    @patch('src.geo_class.requests.get')
    def test_valid_dns(self, mock_get):
        '''
           Tests the case when the ip is valid and it is in the range of valids.
           :param mock_get: The mock of the IP-API json functionality of this method
           :return:
        '''
        dns_information = {'dns': {'geo': 'Israel - BEZEQ-INTERNATIONAL',
                                   'ip': '192.114.75.67'}}
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = dns_information

        # assume
        stub = 'liaztxxwbzl113lsjlx4g4mnbnhhq9mc'

        # expected
        expected = ('Israel - BEZEQ-INTERNATIONAL', '192.114.75.67')

        # action
        result = Geo.dns_details(stub)

        # assert
        self.assertEqual(result, expected)

    @patch('src.geo_class.requests.get')
    def test_empty_dns(self, mock_get):
        '''
           Tests the case when the dns is empty valid.
           :param mock_get: The mock of the IP-API json functionality of this method
           :return:
        '''
        dns_information = {'dns': {'geo': 'Israel - BEZEQ-INTERNATIONAL',
                                   'ip': '192.114.75.67'}}
        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = dns_information

        # assume
        stub = ''

        # expected
        expected = ('Israel - BEZEQ-INTERNATIONAL', '192.114.75.67')

        # action
        result = Geo.dns_details(stub)

        # assert
        self.assertEqual(result, expected)

    def test_too_long_dns(self):
        '''
           Tests the case when the dns is over 32 letters.
           :return:
           '''
        # assume
        stub = '123456781234567812345678123456781'  # 33 letters

        # expected
        expected = 'too long name server'

        # action
        result = Geo.dns_details(stub)

        # assert
        self.assertEqual(result, expected)

    def test_invalid_type(self):
        '''
           Tests the case when the input is not valid.
           :return:
        '''
        # assume
        stub = 123  # not string

        # expected
        expected = 'invalid input'

        # action
        result = Geo.dns_details(stub)

        # assert
        self.assertEqual(result, expected)

    def test_invalid_dns_url_range(self):
        '''
           Tests the case when the url is not valid.
           :return:
        '''
        # assume
        stub = '1!@#$@#$!1234abcbcd1234abcd'  # in range

        # expected
        expected = 'Invalid URL'

        # action
        result = Geo.dns_details(stub)

        # assert
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
