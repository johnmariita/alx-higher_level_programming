#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv) - 1
    if (length == 0):
        print(f"{length:d} arguments.")
    else:
        if (length == 1):
            print(f"{length:d} argument:")
        else:
            print(f"{length:d} arguments:")
        for i in range(1, length + 1):
            print(f"{i:d}: {argv[i]}")


if __name__ == "__main__":
    main()
