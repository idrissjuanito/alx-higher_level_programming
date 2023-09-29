#!/usr/bin/python3
from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    isutf8 = 'OK' if response.headers.get_content_charset() == 'utf-8' else ''
    print('content:', body)
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print("\t- content: ", body)
    print('\t- utf8 content: {}'.format(isutf8))
