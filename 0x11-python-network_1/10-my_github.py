#!/usr/bin/python3
"""a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id"""

import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    print("Number of results: {}".format(results.get("count")))
    [print(r.get("name")) for r in results.get("results")]
