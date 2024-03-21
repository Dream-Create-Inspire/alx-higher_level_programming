#!/usr/bin/python3

# Iterate through the alphabet using ASCII and print without newline
print(''.join(f"{chr(97 + i)}" for i in range(26)), end='')
