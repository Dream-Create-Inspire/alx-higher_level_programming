#!/usr/bin/env python3
def uppercase(s):
    for i in range(len(s)):
        char = s[i]
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # Check if lowercase
            ascii_value -= 32  # Convert to uppercase ASCII value
        print(chr(ascii_value), end='')
    print()  # Print newline

# Test the function
s = "hello, world!"
uppercase(s)
