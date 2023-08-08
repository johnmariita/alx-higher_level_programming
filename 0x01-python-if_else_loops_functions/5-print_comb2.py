#!/usr/bin/python3
for i in range(100):
    if i in range(99):
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
