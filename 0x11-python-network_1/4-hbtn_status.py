#!/usr/bin/python3
""" Fetching with requests library """
import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('- type:', type(res.text))
    print('- content:', res.text)
