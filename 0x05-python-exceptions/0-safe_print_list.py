#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x > len(my_list):
            raise IndexError
        for i in range(x):
            print(my_list[i], end="")
        print("")
        return x
    except:
        for i in my_list:
            print(i, end="")
        print("")
        return len(my_list)
