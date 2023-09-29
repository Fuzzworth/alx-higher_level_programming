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
    for commit in requests.get(url).json():
        if total < 10:
            print(commit_str.format(commit.get("sha"),
                  commit.get("commit").get("author").get("name")))
        total += 1
