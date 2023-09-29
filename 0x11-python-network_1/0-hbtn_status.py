#!/usr/bin/python3
"""
Module Doc
"""
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response
    print(html)
