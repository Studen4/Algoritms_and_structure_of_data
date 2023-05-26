"""Module for sort list by insertion sort algorithm."""


def insertion_sort(my_list):
    """
    Sorts the elements in the MyList object using the insertion sort algorithm.
    Parameters:
    my_list (MyList): The MyList object to be sorted.
    """
    list_length = len(my_list)
    for i in range(1, list_length):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
