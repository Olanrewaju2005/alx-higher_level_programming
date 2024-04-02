#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    """ script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter """
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    param = {'q': letter}
    response = requests.post(url, json=param)

    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                print(f"[{data['id']}] {data['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
