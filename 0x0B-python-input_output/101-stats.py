#!/usr/bin/python3
"""
Module docs
"""


if __name__ == '__main__':
    from sys import stdin

    code_dict = {}
    total_size = 0
    file_size_index = -1
    status_code_index = -2
    valid_index = [200, 301, 400, 401, 403, 404, 405, 500]
    i = 0
    try:
        for line in stdin:
            if i != 0 and i % 10 == 0:
                print("File size: {:d}".format(total_size))
                for c in sorted(code_dict):
                    print("{}: {}".format(c, code_dict[c]))
            stripped = line.split()
            try:
                file_size = int(stripped[file_size_index])
                total_size += file_size
            except (IndexError, ValueError):
                pass
            try:
                code = int(stripped[status_code_index])
            except (IndexError, ValueError):
                pass
            if code in valid_index:
                print(line)
                print(code)
                print(code_dict)
                if code in code_dict:
                    code_dict[code] = code_dict[code] + 1
                else:
                    code_dict[code] = 1
            
            i += 1
        print("File size: {:d}".format(total_size))
        for c in sorted(code_dict):
            print("{}: {}".format(c, code_dict[c]))
    except KeyboardInterrupt as e:
        print("File size: {:d}".format(total_size))
        for c in sorted(code_dict):
            print("{}: {}".format(c, code_dict[c]))
        raise
