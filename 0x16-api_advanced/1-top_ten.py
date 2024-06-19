#!/usr/bin/python3
"""
module that houses a function to return title of hot post in a sub-reddit
"""

import requests


def top_ten(subreddit):
    """
    function to return number of all subscribers of a sub-reddit
    """
    subreddit_name = subreddit  # Replace with the desired subreddit
    sort_type = "hot"  # Choose "hot", "new", or "top"

    base_url = "https://reddit.com/r/"
    url = f"{base_url}{subreddit_name}/{sort_type}.json"

    headers = {"User-Agent": "your_custom_user_agent"}
    payload = {"limit": 10}

    res = requests.get(url, headers=headers, params=payload)

    if res.status_code == 200:
        data = res.json()
        if data["data"]["children"]:
            for post in data["data"]["children"]:
                title = post["data"]["title"]
                print(title)
        else:
            print(None)
                
    else:
        print(None)
