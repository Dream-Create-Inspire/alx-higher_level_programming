#!/usr/bin/python3

#!/usr/bin/python3

def print_last_digit(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    last_digit = abs(number) % 10  # Get the last digit
    print(last_digit, end='')  # Print the last digit
    return last_digit  # Return the last digit

# Test the function
try:
    print_last_digit("Holberton")
except TypeError as e:
    print(e)
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-98)
print(r)
