#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if last_digit > 5:
    str = "and is greater than 5"
elif last_digit == 0:
    str = "and is 0"
elif last_digit < 6 and last_digit not 0:
    str = "and is less than 6 and not 0"

print(f"Last digit of {number:d} is {last_digit:d} {str}")
