#!/usr/bin/python3
"""ask reddit api the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers from a subreddit"""
    path = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": user_agent}
    response = requests.get(path, allow_redirects=False, headers=user_agent)
    if response.status_code in (302, 404):
        return 0
    json = response.json()
    return json.get('data').get('subscribers')
