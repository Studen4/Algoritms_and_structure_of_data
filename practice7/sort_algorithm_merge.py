"""Module for sort list by top-down merge sort algorithm."""
from basepart_list import MyList


def merge_sort_top_down(my_list):
    """
    Sorts the elements in the MyList object using the merge sort algorithm (top-down approach).
    Parameters:
        my_list (MyList): The MyList object to be sorted.
    """
    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    left_half = my_list.get_sublist(0, mid)
    right_half = my_list.get_sublist(mid, len(my_list))

    left_half = merge_sort_top_down(left_half)
    right_half = merge_sort_top_down(right_half)

    merged = merge(left_half, right_half)
    my_list.data = merged.data

    return my_list


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.
    Parameters:
    - left (MyList): The left sorted list.
    - right (MyList): The right sorted list.
    Returns:
    - MyList: The merged sorted list.
    """
    merged = MyList()
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    left.data = merged.data
    return left
