#!/usr/bin/python3
def element_at(my_list, idx):
    if int(idx) < 0:
        return None
    else:
        return my_list[int(idx)]
