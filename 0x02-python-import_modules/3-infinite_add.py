#!/usr/bin/python3
import sys


def main():
    length = len(sys.argv) - 1
    sum = 0
    for i in range(1, length + 1):
        sum += int(sys.argv[i])
    print(f"{sum:d}")


if __name__ == "__main__":
    main()
