#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary).sort()
    print(keys)
    for i in keys:
        print(a_dictionary.get(i))
