#!/usr/bin/env python3
def islower(c):
    if isinstance(c, str) and len(c) == 1:
        return ord('a') <= ord(c) <= ord('z')
    else:
        return False

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))