#!/usr/bin/python3
"""
Module Doc
"""
import urllib.request


with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
   print(html)
