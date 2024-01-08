#!/usr/bin/python3
"""post email"""
import urllib.request
import urllib.parse
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

try:
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send a POST request to the URL
    with urllib.request.urlopen(url, data=data) as response:
        # Decode and print the body of the response
        body = response.read().decode('utf-8')
        print("Response body:")
        print(body)

except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
