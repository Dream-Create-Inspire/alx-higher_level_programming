#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in the list at a specific position.

    Args:
        my_list (list): The original list.
        idx (int): The index where the replacement should occur.
        element: The new element to replace the existing one.

    Returns:
        list: The modified list (if valid index), otherwise the original list.
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
