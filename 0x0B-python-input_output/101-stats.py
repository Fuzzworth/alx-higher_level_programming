#!/usr/bin/python3
"""
Module docs
"""
import sys


def print_stats(code_dict, total_size):
    """
    function doc
    """
    myKeys = list(code_dict.keys())
    myKeys.sort()
    sorted_dict = {p: code_dict[p] for p in myKeys}
    print("File size: {:d}".format(total_size))
    for c in sorted_dict:
        print("{}: {}".format(c, sorted_dict[c]))


def stats():
    """
    function docs
    """
    code_dict = {}
    total_size = 0
    file_size_index = 8
    status_code_index = 7
    valid_index = [200, 301, 400, 401, 403, 404, 405, 500]
    i = 0
    try:
        for line in sys.stdin:
            if i != 0 and i % 10 == 0:
                print_stats(code_dict, total_size)
            stripped = line.split()
            try:
                code = int(stripped[status_code_index])
            except Exception:
                pass
            if code in valid_index:
                if code in code_dict:
                    code_dict[code] = code_dict[code] + 1
                else:
                    code_dict[code] = 1
            try:
                file_size = int(stripped[file_size_index])
            except Exception:
                pass
            total_size += file_size
            i += 1
    except (Exception, KeyboardInterrupt):
        print_stats(code_dict, total_size)


if __name__ == "__main__":
    stats()
