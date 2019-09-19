#!/usr/bin/python3
"""query reddit api"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers from a subreddit"""
    path = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(path, allow_redirects=False, headers=headers)
    if response.status_code in (302, 404):
        return 0

    json = response.json()
    return json.get('data').get('subscribers')
