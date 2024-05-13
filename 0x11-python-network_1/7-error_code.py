#!/usr/bin/python3
"""Error handling in the requests module"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.args[0].split(' ')[0]}")
    else:
        print(response.text)
