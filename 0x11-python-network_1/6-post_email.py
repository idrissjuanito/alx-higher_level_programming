#!/usr/bin/python3
""" sending a post request with requests module """
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.post(argv[1], {'email': argv[2]})
    print(res.text)
