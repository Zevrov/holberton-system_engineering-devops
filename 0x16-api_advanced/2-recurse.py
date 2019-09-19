#!/usr/bin/python3
"""recursively query reddit api"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """recursively return a list of hot post titles for a subreddit"""
    path = "https://www.reddit.com/r/{}/hot.json?after={}&count={}".format(
        subreddit,
        after,
        count)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(path, allow_redirects=False, headers=headers)
    if response.status_code in (302, 404):
        return None

    json = response.json()
    after = json.get('data').get('after')
    count += json.get('data').get('dist')

    if count == 0:
        return None
    for post in json.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, count=count, after=after)
