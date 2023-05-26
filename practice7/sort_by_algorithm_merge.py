"""Module for sort_by list by merge sort algorithm."""
from basepart_list import MyList


def merge_sort_top_down_by_value(my_list, value):
    """
    Sorts the elements in the MyList object by the specified value using
    the top-down merge sort algorithm.
    Parameters:
    - my_list (MyList): The MyList object to be sorted.
    - value: The value to sort the elements by.
    """
    merge_sort_top_down_by_value_recursive(my_list, 0, len(my_list), value)


def merge_sort_top_down_by_value_recursive(my_list, start, end, value):
    """
    Recursively sorts the elements in the MyList object by the specified value using
    the top-down merge sort algorithm.
    Parameters:
    - my_list (MyList): The MyList object to be sorted.
    - start (int): The starting index of the sublist to be sorted.
    - end (int): The ending index of the sublist to be sorted.
    - value: The value to sort the elements by.
    """
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort_top_down_by_value_recursive(my_list, start, mid, value)
        merge_sort_top_down_by_value_recursive(my_list, mid, end, value)
        merge(my_list, start, mid, end, value)


def merge(my_list, left, mid, right, value):
    """
    Merges two sorted sub-lists into a single sorted sublist.

    Parameters:
    - my_list (MyList): The MyList object containing the elements.
    - left (int): The left index of the first sublist.
    - mid (int): The right index of the first sublist and left index of the second sublist.
    - right (int): The right index of the second sublist.
    - value: The value to sort the elements by.
    """
    merged = MyList()
    i = left
    j = mid
    while i < mid and j < right:
        if my_list[i][value] <= my_list[j][value]:
            merged.append(my_list[i])
            i += 1
        else:
            merged.append(my_list[j])
            j += 1

    while i < mid:
        merged.append(my_list[i])
        i += 1

    while j < right:
        merged.append(my_list[j])
        j += 1

    for k in range(left, right):
        my_list[k] = merged[k - left]
