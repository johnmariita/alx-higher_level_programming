#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        total, divider = 0, 0
        for tup in my_list:
            total += (tup[0] * tup[1])
            divider += (tup[1])
        return (total/divider)
    return 0
