"""Module for sort list by bubble sort algorithm."""


def bubble_sort(my_list):
    """
    Sorts the elements in the MyList object using the bubble sort algorithm.

    Parameters:
    - my_list (MyList): The MyList object to be sorted.
    """
    list_length = len(my_list)
    for i in range(list_length - 1):
        for j in range(list_length - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
