#!/usr/bin/python3
""" send urllib request with some data """
import sys
from urllib import request

if __name__ == "__main__":
    req = request.Request(
            url=sys.argv[1],
            data=sys.argv[2].encode('utf-8'),
            method='POST')
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
