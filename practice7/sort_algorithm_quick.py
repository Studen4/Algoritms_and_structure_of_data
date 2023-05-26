"""Module for sort list by quick sort algorithm."""
from basepart_list import MyList


def quick_sort_recursive(my_list):
    """
    Sorts the elements in the MyList object using the quick sort algorithm (recursive approach).
    Parameters:
        my_list (MyList): The MyList object to be sorted.
    """
    if len(my_list) <= 1:
        return my_list

    divider = my_list[0]
    smaller_elements = MyList()
    greater_elements = MyList()

    for i in range(1, len(my_list)):
        if my_list[i] <= divider:
            smaller_elements.append(my_list[i])
        else:
            greater_elements.append(my_list[i])

    sorted_smaller = quick_sort_recursive(smaller_elements)
    sorted_greater = quick_sort_recursive(greater_elements)

    sorted_list = MyList()

    for item in sorted_smaller:
        sorted_list.append(item)

    sorted_list.append(divider)

    for item in sorted_greater:
        sorted_list.append(item)

    my_list.data = sorted_list.data
    return sorted_list
