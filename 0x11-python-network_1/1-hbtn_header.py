#!/usr/bin/python3
""" display request id"""
import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the headers.")
