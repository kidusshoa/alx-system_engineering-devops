#!/usr/bin/python3

"""
Reddit Subreddit Subscriber Counter

This script defines a function that queries the Reddit API and returns the number of subscribers
(total subscribers, not active users) for a given subreddit. If an invalid subreddit is provided,
the function returns 0.

Dependencies:
    - requests: Python HTTP library for making API requests

Usage:
    - Ensure the 'requests' library is installed: pip install requests
    - Call the 'number_of_subscribers' function with the desired subreddit name.

Example:
    subscribers_count = number_of_subscribers('python')
    print(f'The subreddit has {subscribers_count} subscribers.')

Author:
    Your Name

"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The total number of subscribers for the subreddit. Returns 0 if the subreddit is invalid.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
