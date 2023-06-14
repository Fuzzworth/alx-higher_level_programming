#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        new_dict = {}
        for key, val in a_dictionary.items():
            if value == val:
                new_dict[key] = value
        for key, val in new_dict.items():
            del a_dictionary[key]
        return new_dict
    else:
        return a_dictionary
