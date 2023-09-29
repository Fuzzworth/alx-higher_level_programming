#!/usr/bin/python3
"""
Module Doc
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()
    header = response.getheader("Content-type")
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print(f"\t- content: {html}")
    if "utf-8" in header:
        print("\t- utf8 content: {}".format("OK"))
    else:
        print("\t- utf8 content: {}".format("BAD"))
