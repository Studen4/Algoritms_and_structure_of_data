"""Module for sort_by list by quick sort algorithm."""


def quick_sort_iterative(my_list, value):
    """
    Sorts the elements in the MyList object by the specified value
    using the iterative quick sort algorithm.
    Parameters:
    - my_list (MyList): The MyList object to be sorted.
    - value: The value to sort the elements by.
    """
    stack = [(0, len(my_list) - 1)]
    while stack:
        start, end = stack.pop()
        while start < end:
            pivot = my_list[end][value]
            i = start - 1
            for j in range(start, end):
                if my_list[j][value] <= pivot:
                    i += 1
                    my_list[i], my_list[j] = my_list[j], my_list[i]
            my_list[i + 1], my_list[end] = my_list[end], my_list[i + 1]
            if i - start < end - i - 2:
                stack.append((i + 2, end))
                end = i
            else:
                stack.append((start, i))
                start = i + 2
