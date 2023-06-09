#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if int(idx) < 0:
        return my_list
    elif int(idx) > (len(my_list) - 1):
        return None
    else:
        new_list = my_list.copy()
        new_list[int(idx)] = element
        return new_list
