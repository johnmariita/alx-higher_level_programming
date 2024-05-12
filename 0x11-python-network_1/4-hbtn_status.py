#!/usr/bin/python3
"""A GET request using requests module"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body Response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
