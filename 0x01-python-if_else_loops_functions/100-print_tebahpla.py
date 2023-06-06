#!/usr/bin/python3
print_higher = False
for char_number in range(97, 123):
    if print_higher:
        char_number = char_number + int((ord('a') - ord('A')))
    print("{character}".format(character=chr(char_number)), end="")
    print_higher = not print_higher
