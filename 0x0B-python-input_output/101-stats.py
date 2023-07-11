#!/usr/bin/python3
"""
Module docs
"""
import sys


i = 0
code_dict = {}
total_size = 0
file_size_index = 8
status_code_index = 7
try:
    for line in sys.stdin:
        if i != 0 and i % 10 == 0:
            myKeys = list(code_dict.keys())
            myKeys.sort()
            sorted_dict = {p: code_dict[p] for p in myKeys}
            print(f"File size: {total_size}")
            for c in sorted_dict:
                print("{}: {}".format(c, sorted_dict[c]))
        stripped = line.split()
        code = stripped[status_code_index]
        file_size = stripped[file_size_index]
        if code in code_dict:
            code_dict[code] = code_dict[code] + 1
        else:
            code_dict[code] = 1
        total_size += int(file_size)
        i += int(1)
except KeyboardInterrupt:
    myKeys = list(code_dict.keys())
    myKeys.sort()
    sorted_dict = {p: code_dict[p] for p in myKeys}
    print(f"File size: {total_size}")
    for c in sorted_dict:
        print("{}: {}".format(c, sorted_dict[c]))
