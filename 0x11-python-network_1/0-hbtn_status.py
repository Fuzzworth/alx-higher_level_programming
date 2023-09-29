#!/usr/bin/python3
"""
Module Doc
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print(f"\t- content: {html}")
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
