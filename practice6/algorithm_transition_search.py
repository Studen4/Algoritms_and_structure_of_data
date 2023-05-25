"""Module with algorithm of jump (transition) search."""
from math import sqrt


def jump_search(doubly_linked_list, target):
    """
    Perform jump search on a doubly linked list to find the target element.
    Args:
        doubly_linked_list: The doubly linked list to search in.
        target: The element to search for.
    Returns:
        True if the target element is found, False otherwise.
    """
    size = doubly_linked_list.get_size()
    step = int(sqrt(size))
    prev = None
    current = doubly_linked_list.head

    while current is not None and current.data < target:
        prev = current
        for _ in range(step):
            current = current.next
            if current is None:
                break

    if prev is None:
        current = doubly_linked_list.head
    else:
        current = prev.next

    while current is not None and current.data <= target:
        if current.data == target:
            return True
        current = current.next

    return False
