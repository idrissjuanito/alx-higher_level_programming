#!/usr/bin/python3
""" querying github api for user infor """
import requests
from sys import argv

if __name__ == "__main__":
    heads = {'Authorization': 'Bearer {}'.format(argv[2]),
             'X-GitHub-Api-Version': '2022-11-28',
             'Accept': 'application/vnd.github+json'}
    res = requests.get(' https://api.github.com/user',
                       headers=heads, params={'username': argv[1]})
    if res.status_code == 200:
        r = res.json()
        print(r['id'])
    else:
        print(None)
