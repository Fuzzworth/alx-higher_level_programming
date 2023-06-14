#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    for top, bottom in my_list:
        numerator += (top * bottom)
        denominator += bottom
    return numerator / denominator
