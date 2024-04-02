#!/usr/bin/python3

import sys
import requests

def get_usr_id(username, token):
    """ function returns user id """
    url = f"https://api.github.com/users/{username}"
    header = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(f"{user_id}")
    else:
        print("None")

if __name__ == "__main__":
    """ Takes two arguments from user: Username and Personal Access Token """
    username = sys.argv[1]
    token = sys.argv[2]
    get_usr_id(username, token)
