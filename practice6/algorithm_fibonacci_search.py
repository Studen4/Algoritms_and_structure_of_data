"""Module with algorithm of Fibonacci search."""


def fibonacci_search(doubly_linked_list, target):
    """
    Perform Fibonacci search on a sorted doubly linked list
    to find the target element.
    Args:
        doubly_linked_list: The sorted doubly linked list to search in.
        target: The element to search for.
    Returns:
        True if the target element is found, False otherwise.
    """
    size = doubly_linked_list.get_size()

    fib2 = 0  # F(i-2)
    fib1 = 1  # F(i-1)
    fib = fib2 + fib1  # F(i)

    while fib < size:
        fib2, fib1 = fib1, fib
        fib = fib2 + fib1

    index = 0

    while fib > 0:
        if index + fib < size:
            current = doubly_linked_list.get_node_at_index(index + fib)
            if current.data == target:
                return True
            if current.data < target:
                index += fib
        fib2, fib1 = fib1 - fib2, fib2
        fib = fib2 + fib1

    return False
