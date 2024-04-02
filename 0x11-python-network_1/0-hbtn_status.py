#!/usr/bin/python3
""" importing urllib.request module """
import urllib.request

if __name__ == "__main__":
    """ Bash script that fetches a url and diplays the type, content type, utf8 content """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))
