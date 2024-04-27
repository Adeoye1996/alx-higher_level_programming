#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        print(response.text)
