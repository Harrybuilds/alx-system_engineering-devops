#!/usr/bin/python3
"""
module that houses function to
retrive title of top ten post of a
given subreddit
"""

from pprint import pprint
from requests import get
""" import necessary dependencies """


def top_ten(subreddit):
    """
    function to get top 10 hot post
    title on a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    user_agent = {'User-agent': 'CLI'}
    payload = {'limit': 10}

    res = get(url, headers=user_agent, params=payload)

    if res.status_code == 200:
        data = res.json()
        if data.get('data').get('children'):
            for post in data.get('data').get('children'):
                title = post['data']['title']
                print(title)
        else:
            print(None)
    else:
        print(None)
