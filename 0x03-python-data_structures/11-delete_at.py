#!/usr/bin/python3

# Checker 4
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    return my_list[:idx] + my_list[idx + 1:]

# Checker 5
def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]

# Checker 6
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()

