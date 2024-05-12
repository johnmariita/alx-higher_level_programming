#!/usr/bin/python3
"""HTTP error handling"""

import sys
import urllib.request
import urllib.error.HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
