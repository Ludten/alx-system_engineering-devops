#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Print the titles of the first 10 hot posts listed for the subreddit
    recursively
    """
    url = "https://reddit.com/r/" + subreddit + \
        "/hot.json?limit=100&after={}".format(after)
    headers = {'User-Agent': 'Mozilla/5.0'}
    post = requests.get(url=url, headers=headers, allow_redirects=False)
    tpost = requests.get(
        url=post.headers['Location'], headers=headers, allow_redirects=False)
    if tpost.status_code != 200:
        return None
    else:
        tposts = tpost.json()['data']['children']
        for toppost in tposts:
            hot_list.append(toppost['data']['title'])
        aft = tpost.json()['data']['after']
        if aft is not None:
            recurse(subreddit, hot_list, aft)
        else:
            return hot_list
    return hot_list
