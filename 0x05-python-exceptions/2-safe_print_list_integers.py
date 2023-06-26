#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        while x > 0:
            if type(my_list[x]) == int):
                print("{}".format(my_list[count]), end="")
                count += 1
                x -= 1
        print("")
    except Exception:
        print("")
    return count
