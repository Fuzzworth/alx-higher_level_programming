#!/usr/bin/python3
print_higher = False
for char_number in range(97, 123):
    if print_higher:
        char_number = char_number + (ord('a') - ord(-'A'))
        print_higher = !print_higher
    print("{character}".format(character=chr(char_number)), end="")
