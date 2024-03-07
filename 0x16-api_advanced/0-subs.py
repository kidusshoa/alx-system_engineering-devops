#!/usr/bin/python3
"""Write a function that queries the Reddit API and
   returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """A function that returns the number of subscribers for a
    given subreddit"""
    user_agent = "0-subs/1.0"
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return 0
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit)
        print(f"{subscribers_count}")

