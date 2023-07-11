#!/usr/bin/python3
"""
Module docs
"""
import sys


i = 0
code_dict = {}
total_size = 0
for line in sys.stdin:
    if i != 0 and i % 10 == 0:
        print(f"File size: {total_size}")
        for i in code_dict:
            print("{}: {}".format(i, code_dict[i]))
        code_dict.clear()
        total_size = 0
    stripped = line.strip(" ")
    file_size_index = 8
    status_code_index = 7
    code = int(stripped[status_code_index])
    if code in code_dict:
        code_dict[code] = code_dict[code] + 1
    else:
        code_dict[code] = 1
    total_size += int(stripped[file_size_index])
    print(f"{code} {total_size}")
    i += 1
