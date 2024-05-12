#!/usr/bin/python3
"""A script that sends a GET request"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    print("Body Response")
    print(f"    -type: {type(body)}")
    print(f"    -content: {body}")
    print(f"    -utf8 content: {body.decode('utf-8')}")
