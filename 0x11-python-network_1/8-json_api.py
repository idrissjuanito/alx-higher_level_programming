#!/usr/bin/python3
""" sending request and parsing json response """
import requests
from sys import argv

if __name__ == "__main__":
    val = argv[1] if len(argv) > 1 else ""
    res = requests.post('http://0.0.0.0:5000/search_user', params={'q': val})
    try:
        r = res.json()
        if len(r.keys()) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(r['id'], r['name']))
    except requests.exceptions.InvalidJSONError as e:
        print('Not a valid JSON')
