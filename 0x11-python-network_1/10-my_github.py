#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    res = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
