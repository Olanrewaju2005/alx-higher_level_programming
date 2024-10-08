#!/usr/bin/python3
"""
import important modules
"""
import requests


def number_of_subscribers(subreddit):
    """
    function queries reddit api and returns the number
    of subcribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")