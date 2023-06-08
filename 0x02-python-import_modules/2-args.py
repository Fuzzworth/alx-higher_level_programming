#!/usr/bin/python3
from sys import argv
arg_str_0 = "arguments."
arg_str_1 = "argument:"
arg_str_n = "arguments:"
argc = len(argv)


def print_args():
    for i in range(argc):
        print("{:d}: {}".format(i + 1, argv[i]))


if __name__ == "__main__":
    if (argc == 0):
        print("{:d} {}".format(argc, arg_str_0))
    elif (argc == 1):
        print("{:d} {}".format(argc, arg_str_1))
        print_args()
    else:
        print("{:d} {}".format(argc, arg_str_n))
        print_args
