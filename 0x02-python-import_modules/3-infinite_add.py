#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = sum(int(arg) for arg in argv[1:])
    print(total)
