#!/usr/bin/python3
"""
Module Docs
"""
from sys import argv
from urllib.error import HTTPError
from urllib.request import urlopen, Request


if __name__ == "__main__":
    try:
        with urlopen(Request(argv[1])) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as exception:
        print('Error code:', exception.code)
