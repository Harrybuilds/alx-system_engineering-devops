#!/usr/bin/python3
"""
module that houses a function that
queries reddit API and gets the
total number of subscribers of a
given sub-reddit
"""

import requests
"""import all necessary dependencies"""


def number_of_subscribers(subreddit):
    """function that handles the quering"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = {'User-agent': 'CLI'}

    data = requests.get(url, headers=user_agent)

    if data:
        sub_py_dict = data.json()

        res_data = sub_py_dict.get('data')

        sub = res_data.get('subscribers', 0)

        return sub

    return 0
