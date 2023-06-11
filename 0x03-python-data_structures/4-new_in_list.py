#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if int(idx) < 0 orint(idx) > (len(my_list) - 1):
        return my_list
    else:
        new_list = my_list.copy()
        new_list[int(idx)] = element
        return new_list
