#!/usr/bin/python3
"""
Takes your GitHub credentials (username and personal access token) and uses the GitHub API
to display your id
"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("Error:", response.status_code)
