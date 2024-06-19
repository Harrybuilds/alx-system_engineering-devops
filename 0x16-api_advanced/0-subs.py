#!/usr/bin/python3
"""
module that g
housrs a function to return number of all subscribers of a sub-reddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    function to return number of all subscribers of a sub-reddit
    """
    url = f"https://reddit.com/r/{subreddit}/hot.json"

    # Additional options (optional):
    headers = {"User-Agent": "your_custom_user_agent"}
    params = {"limit": 10}  # Limit the number of posts returned

    # Send the GET request
    res = requests.get(url, headers=headers, params=params)

    # Check for successful response
    if res.status_code == 200:
        # Parse the JSON response
        data = res.json()

        if data['data']['children']:
            data_only = data['data']['children'][-1]['data']
            return data_only['subreddit_subscribers']
        else:
            return 0
    else:
        return 0
