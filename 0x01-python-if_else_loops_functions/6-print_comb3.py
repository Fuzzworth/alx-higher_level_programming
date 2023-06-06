#!/usr/bin/python3
for first_number in range(10):
    for second_number in range(10):
        if first_number < second_number and first_number != second_number:
            print("{one}{two}".format(one=first_number,two=second_number), sep=", ")
