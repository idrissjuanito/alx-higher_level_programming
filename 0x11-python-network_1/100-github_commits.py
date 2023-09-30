#!/usr/bin/python3
""" querying github api for user infor """
import requests
from sys import argv

if __name__ == "__main__":
    heads = {'X-GitHub-Api-Version': '2022-11-28',
             'Accept': 'application/vnd.github+json'}
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    res = requests.get(url, headers=heads, params={'per_page': 10})
    r = res.json()
    if len(r) != 0:
        for commit in r:
            print('{}: {}'.format(commit['sha'],
                                  commit['commit']['author']['name']))
