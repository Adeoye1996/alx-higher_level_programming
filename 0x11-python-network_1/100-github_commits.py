#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of the repository and owner
sent in as arguments
"""

import requests
import sys

if __name__ == '__main__':
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print(f"Error: {response.status_code}")
