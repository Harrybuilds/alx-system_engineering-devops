#!/usr/bin/python3
"""
module that houses a function to return number of all subscribers of a sub-reddit using the reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    function to return number of all subscribers of a sub-reddit
    """
    url = f"https://reddit.com/r/{subreddit}/about.json"

    # Additional options (optional):
    headers = {"User-Agent": "python script"}
    params = {"limit": 10}  # Limit the number of posts returned

    # Send the GET request
    res = requests.get(url, headers=headers, params=params)

    # Check for successful response
    if res.status_code == 200:
        # Parse the JSON response
        data = res.json()

        sub = data.get("data", {}).get("subscribers", 0)
        return sub
    else:
        return 0
