#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if int(idx) < 0 or int(idx) > (len(my_list) - 1):
        return my_list
    else:
        my_list[int(idx)] = element
        return my_list
