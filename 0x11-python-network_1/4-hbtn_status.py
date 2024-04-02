#!/usr/bin/python3
""" import of requests module """
import requests

if __name__ == "__main__":
    """ script fetches https://alx-intranet.hbtn.io/status """
    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)

    if req.status_code == 200:
        print("Body response:")
        print(f"\t- type: {type(req.text)}")
        print(f"\t- content: {req.text}")
