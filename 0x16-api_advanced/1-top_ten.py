#!/usr/bin/python3
"""query reddit api"""
import requests


def top_ten(subreddit):
    """return top ten hot posts from a subreddit"""
    path = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(path, allow_redirects=False, headers=headers)
    if response.status_code in (302, 404):
        print("None")
        return

    json = response.json()
    json_children = json.get('data').get('children')
    for post in json_children:
        print(post.get('data').get('title'))
