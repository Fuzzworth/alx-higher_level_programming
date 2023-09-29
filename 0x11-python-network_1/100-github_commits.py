#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
import requests


if __name__ == "__main__":
    total = 0
    commit_str = "{}: {}"
    url = "https://api.github.com/repos/{}/{}/commits"
    formated_url = url.format(argv[2], argv[1])
    for commit in requests.get(formated_url).json():
        if total < 10:
            sha = commit.get("sha")
            name = commit.get("commit").get("author").get("name")
            print(commit_str.format(sha, name))
        total += 1
