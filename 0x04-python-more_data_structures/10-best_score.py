#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        dict_items = a_dictionary.items()
        print(dict_items[0])
        max_key, max_value = dict_items[0]
        for key, value in dict_items:
            if value > max_value:
                max_key, max_value = key, value
        return max_key
    else:
        return None
