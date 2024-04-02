#!/usr/bin/python3
""" import of important modules """
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    """ script that takes in a URL, sends a request to the URL and displays the body of the response """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as er:
        print(f"Error code: {er.code}")
