#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    response = requests.post(url, data=data)

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
