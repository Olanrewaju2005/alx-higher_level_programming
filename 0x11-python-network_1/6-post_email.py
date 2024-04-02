#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    """ script that takes in a URL and an email address,
    sends a POST request to the passed URL with the email
    as a parameter, and finally displays the body of the response """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        body = response.text()
        print(body)
