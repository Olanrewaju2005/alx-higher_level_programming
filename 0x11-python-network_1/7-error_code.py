#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    """
    script that takes in a URL, sends a request
    to the URL and displays the body of the response 
    """
    url = sys.argv[1]
    request = requests.get(url)

    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)
