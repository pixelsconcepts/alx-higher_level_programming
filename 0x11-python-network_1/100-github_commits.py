#!/usr/bin/python3
"""list commits from repo"""
import requests
import sys

def list_commits(repo_name, owner_name):
    """ list all commits """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        commits = response.json()

        for commit in reversed(commits):
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    """don't run if imported"""
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    list_commits(repo_name, owner_name)
