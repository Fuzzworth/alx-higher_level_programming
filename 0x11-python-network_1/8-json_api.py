#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    c = ""
    if len(argv) > 1:
        c = {"q": argv[1][0]}
    req = requests.post(url, data=c)
    try:
        res = req.json()
        if res:
            str_re = "[{}] {}"
            print(str_re.format(res.get("id"), res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
