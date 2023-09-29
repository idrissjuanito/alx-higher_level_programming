#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.headers.get('X-Request-Id'))
