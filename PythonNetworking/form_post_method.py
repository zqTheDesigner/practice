#! python3

import requests

data_dictionary = {'custname':'customer', 'custtel':'323232', 'size':'large', 'custemail':'email@domain.com'}

response = requests.post('https://httpbin.org/post', data='test')

print(response.status_code)

print(response.text)