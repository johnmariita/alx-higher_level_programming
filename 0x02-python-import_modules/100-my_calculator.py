#!/usr/bin/python3
import sys
import calculator_1


def main():
    length = len(sys.argv) - 1
    if (length != 3):
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print(f"{sys.argv[1]} + {sys.argv[3]} = {calculator_1.add(a, b)}")
        exit(0)
    if sys.argv[2] == '-':
        print(f"{sys.argv[1]} - {sys.argv[3]} = {calculator_1.sub(a, b)}")
        exit(0)
    if sys.argv[2] == '*':
        print(f"{sys.argv[1]} * {sys.argv[3]} = {calculator_1.mul(a, b)}")
        exit(0)
    if sys.argv[2] == '/':
        print(f"{sys.argv[1]} / {sys.argv[3]} = {calculator_1.div(a, b)}")
        exit(0)


if __name__ == "__main__":
    main()
