'''
Authors: Almog Mahluf - 205490170
         Alon Gabay   - 2080646080
         Michael Elisha -
'''

import requests
class Geo:
    '''
    This Class uses IP-API
    We serve our data in multiple formats via a simple URL-based interface over HTTP,
    which enables you to use our data directly from a user's browser or from your server.
    '''
    @staticmethod
    def ip_details(ip_name):
        '''
        :param ip_name: ip address like '10.0.0.1'
        :return:(country code, city, isp, query) if the ip is valid
                 else if the ip query is invalid None else a message.
        '''
        ip_address = 'http://ip-api.com/json/'
        ip_address = ip_address + ip_name
        api_result = requests.get(ip_address)
        api_response = api_result.json()
        if 'country' in api_response:
            return (api_response['countryCode'],
                    api_response['city'],
                    api_response['isp'], api_response['query'])

        if api_response['message'] == 'invalid query':
            return None
        return api_response['message']

    @staticmethod
    def ip_isp_name(ip_name):
        '''
        :param ip_name: ip address like '10.0.0.1'
        :return: the isp of the current ip if the ip is valid
                 else a message.
        '''
        ip_address = 'http://ip-api.com/json/'
        ip_address = ip_address + ip_name
        api_result = requests.get(ip_address)
        api_response = api_result.json()
        if api_response['status'] == 'success':
            return api_response['isp']
        return api_response['status']


    #
    # @staticmethod
    # def is_ip_in_country(ip_name, country_name):
    #     return (Geo.ip_current_temp(ip_name)['country']) == country_name

# http://edns.ip-api.com/json
        # http://edns.ip-api.com/json
    @staticmethod
    def dns_details(host_name):
        '''

        :param host_name: name server
        :return:
        '''
        try:
            url_address = 'http://'
            if isinstance(host_name, str) is False:
                return 'invalid input'
            url_address = url_address + host_name
            if len(host_name) > 32:
                return 'too long name server'
            if len(host_name) > 0 and len(host_name) <= 32:
                url_address = url_address + '.edns.ip-api.com/json'
            if len(host_name) == 0:
                url_address = url_address + 'edns.ip-api.com/json'

            api_result = requests.get(url_address)
            api_response = api_result.json()
        except requests.exceptions.InvalidURL:
            return 'Invalid URL'
        #return api_response
        return (api_response['dns']['geo'], api_response['dns']['ip'])

# print(Geo.ip_details('8.8.8'))

# print(Geo.ip_isp_name('8.8.8'))

# print(Geo.is_ip_in_country('8.8.8.8','United States'))

# liaztxxwbzl113lsjlx4g4mnbnhhq9mc

# 123456781234567812345678123456781

print(Geo.dns_details('1!@#$@#$!1234abcbcd1234abcd'))
