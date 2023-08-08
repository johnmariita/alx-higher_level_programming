#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = -number
    else:
        num = number
    print("{}".format(num % 10), end="")
    return num % 10
