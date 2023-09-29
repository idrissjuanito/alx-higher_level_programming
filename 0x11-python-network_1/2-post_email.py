#!/usr/bin/python3
""" send urllib request with some data """
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(
            url=sys.argv[1],
            data=urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii'),
            method='POST')
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
