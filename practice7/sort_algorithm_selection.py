"""Module for sort list by selection sort algorithm."""


def selection_sort(my_list):
    """
    Sorts the elements in the MyList object using the selection sort algorithm.
    Parameters:
    my_list (MyList): The MyList object to be sorted.
    """
    list_length = len(my_list)
    for i in range(list_length - 1):
        min_index = i
        for j in range(i + 1, list_length):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
