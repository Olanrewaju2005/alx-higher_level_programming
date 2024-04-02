#!/usr/bin/python3
""" import of some important moduled """
import requests
import sys

if __name__ == "__main__":
    """ script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header """
    url = sys.argv[1]
    response = requests.get(url)
    response_id = response.headers.get('X-Request-Id')

    if response_id:
        print(response_id)
