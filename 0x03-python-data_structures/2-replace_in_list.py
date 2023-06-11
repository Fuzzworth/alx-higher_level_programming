#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if int(idx) < 0 or int(idx) > (len(my_list)):
        return mylist
    else:
        my_list[int(idx)] = element
        return my_list
