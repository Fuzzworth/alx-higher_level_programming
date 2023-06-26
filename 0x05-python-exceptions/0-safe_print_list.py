#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while x >= 0:
            print("{}".format(i), end="")
            count += 1
            x -= 1
        print("")
    except Error:
        print("Error")
    return count
