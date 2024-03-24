#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in the list at a specific position without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): The index where the replacement should occur.
        element: The new element to replace the existing one.

    Returns:
        list: A new list with the modified element (if valid index), otherwise a copy of the original list.
    """
    if idx >= 0 and idx < len(my_list):
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    else:
        return my_list
