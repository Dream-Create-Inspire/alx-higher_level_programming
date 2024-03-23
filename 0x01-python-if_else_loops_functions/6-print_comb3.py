#!/usr/bin/python3

# Iterate through the first digit
for i in range(10):
    # Iterate through the second digit
    for j in range(i + 1, 10):
        print("{:d}{:d}".format(i, j), end=", " if i < 8 or j < 9 else "\n")
