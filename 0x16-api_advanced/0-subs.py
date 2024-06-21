#!/usr/bin/python3
"""
module that houses a function to return number
of all subscribers of a sub-reddit using the reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'custom agent'}

    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(url, headers=headers).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
