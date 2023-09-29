#!/usr/bin/python3
from urllib import request
from sys import argv

with request.urlopen(argv[1]) as res:
    print(res.headers['X-Request-Id'])
