#!/usr/bin/python3
"""Queries the Reddit API"""


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for the subreddit
    """
    import requests
    url = "https://reddit.com/r/" + subreddit + "/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    sub = requests.get(url=url, headers=headers, allow_redirects=False)
    subctr = requests.get(
        url=sub.headers['Location'], headers=headers, allow_redirects=False)
    if subctr.status_code != 200:
        return 0
    return subctr.json()['data']['subscribers']
