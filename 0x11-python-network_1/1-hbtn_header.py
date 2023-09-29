#!/usr/bin/python3
""" extract request header from urllib request """
import sys
from urllib import request

with request.urlopen(sys.argv[1]) as res:
    print(res.headers.get('X-Request-Id'))
