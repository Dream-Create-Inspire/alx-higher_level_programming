#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers in the list, in reverse order."""
    for num in reversed(my_list):
        print("{}".format(num))
