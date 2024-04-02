#!/usr/bin/python3

import urllib.request
import sys

if __name__ == "__main__":
    """ Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response. """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(f"{request_id}")
