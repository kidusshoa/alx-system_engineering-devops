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
    # Form the API request URL for the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid potential API access issues
    headers = {"User-Agent": "Custom"}
    
    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the subscriber count from the JSON response
        subscribers_count = response.json().get("data", {}).get("subscribers", 0)
        return subscribers_count
    else:
        # Invalid subreddit or API request failure, return 0
        return 0



