#!/usr/bin/python3
'''
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.
'''

import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        print(r.text)
    elif r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
