#!/usr/bin/python3
""" send urllib request with some data """
from sys import argv
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(
            url=argv[1],
            data=urllib.parse.urlencode({'email': argv[2]}).encode('utf-8'),
            method='POST')
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
