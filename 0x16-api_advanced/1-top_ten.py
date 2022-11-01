#!/usr/bin/python3
"""Queries the Reddit API"""


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for the subreddit
    """
    import requests
    url = "https://reddit.com/r/" + subreddit + "/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}
    post = requests.get(url=url, headers=headers, allow_redirects=False)
    tpost = requests.get(
        url=post.headers['Location'], headers=headers, allow_redirects=False)
    if tpost.status_code != 200:
        print(None)
    else:
        tposts = tpost.json()['data']['children']
        for toppost in tposts:
            print(toppost['data']['title'])
