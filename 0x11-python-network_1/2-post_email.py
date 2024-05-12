#!/usr/bin/python3
"""A script that sends a post request"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    en_data = urllib.parse.urlencode(data)
    en_data = en_data.encode('ascii')
    with urllib.request.urlopen(url, en_data) as response:
        print(response.read().decode('utf-8'))
