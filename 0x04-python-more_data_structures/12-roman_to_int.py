#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if roman_string:
        total_sum = 0
        roman_string[::-1]
        print(roman_string)
        last_key = 0
        current_key = 0
        for symbol in roman_string:
            current_key = roman_dict.get(symbol, 0)
            if last_key != 0 and last_key > current_key:
                total_sum -= current_key
            elif last_key != 0 and last_key >= current_key:
                total_sum += current_key
            elif last_key == 0:
                total_sum += current_key
            last_key = current_key
        return total_sum
    else:
        return 0
