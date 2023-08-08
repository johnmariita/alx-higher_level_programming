#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        fb = ""
        if (i % 3 == 0):
            fb = "Fizz"
        if (i % 5 == 0):
            fb += "Buzz"
        elif i % 3 != 0 and i % 5 != 0:
            fb = i
        print("{}".format(fb), end=" ")
