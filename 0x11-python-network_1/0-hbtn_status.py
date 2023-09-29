#!/usr/bin/python3
from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print("\t- content:", body)
    print('\t- utf8 content: {}'.format(body.decode('utf-8')))
