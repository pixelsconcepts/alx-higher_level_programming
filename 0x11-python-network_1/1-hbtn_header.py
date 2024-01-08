#!/usr/bin/python3
import urllib.request
import sys

def get_x_request_id(url):
    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as response:
            # Retrieve the value of the X-Request-Id from the headers
            x_request_id = response.getheader('X-Request-Id')

            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id not found in the headers.")
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")

if __name__ == "__main__":
    # Check if a URL is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    # Call the function to retrieve and display X-Request-Id
    get_x_request_id(url)

