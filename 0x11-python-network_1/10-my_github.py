#!/usr/bin/python3
'''
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''

import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = 'https://api.githup.com/user'

    
    r = requests.get(url, auth=(username, password))
    print(r.json().get('id'))
