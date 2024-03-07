#!/usr/bin/python3
'''
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        letter = ''
    else:
        letter = argv[1]

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})

    try:
        dir = r.json()
        if dir == {}:
            print('No result')
        else:
            print('[{}] {}'.format(dir.get('id'), dir.get('name')))
    except ValueError:
        print('Not a valid JSON')
