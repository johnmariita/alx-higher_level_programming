#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv) - 1
    if (length == 0):
        print(f"{length:d} arguments.")
    else:
        if (length == 1):
            print(f"{length:d} argument")
        else:
            print(f"{length:d} arguments")
        for i in range(1, length + 1):
            print(f"{i:d}: {sys.argv[i]}")


if __name__ == "__main__":
    main()
