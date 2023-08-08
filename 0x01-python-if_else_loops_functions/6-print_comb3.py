#!/usr/bin/python3
def rev(x):
    ones = x % 10
    tenths = x // 10
    return (ones * 10) + tenths


for i in range(100):
    if rev(i) < i or rev(i) == i:
        continue
    if (i == 89):
        print("{:02}".format(i))
    else:
        print("{:02}".format(i), end=", ")
