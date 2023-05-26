"""Module for sort_by list by bubble sort algorithm."""


def bubble_sort_with_cycles(my_list, value):
    """
    Sorts the elements in the MyList object by the specified value using the bubble sort algorithm
    with while loop and break statement.
    Parameters:
    - my_list (MyList): The MyList object to be sorted.
    - value: The value to sort the elements by.
    """
    list_length = len(my_list)
    for _ in range(list_length - 1):
        sorted_flag = True
        current = my_list.data
        while current.next is not None:
            if current.value[value] > current.next.value[value]:
                current.value, current.next.value = current.next.value, current.value
                sorted_flag = False
                break
            current = current.next
        if sorted_flag:
            break
