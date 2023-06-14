#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dictionary = a.a_dictionary.copy()
    if key in new_dictionary:
        new_dictionary.update(key=value)
    else:
        new_dictionary[key] = value
    return new_dictionary
