#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list and search and replace:
        return [replace if i == search else i for i in my_list]
