#!/usr/bin/python3
""" import of important modules """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """ script takes two parameters and displays the body as response """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    
    with urllib.request.urlopen(req) as response:
        decoded_response = response.read().decode('utf-8')
        print(decoded_response)
