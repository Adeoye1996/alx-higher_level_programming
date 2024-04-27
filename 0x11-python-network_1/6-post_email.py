#!/usr/bin/python3
""""
    Takes in a URL and an email address
    Sends a POST request to the passed URL with the email as a parameter
    Displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
