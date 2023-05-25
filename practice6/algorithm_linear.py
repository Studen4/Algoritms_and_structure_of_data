"""Module with algorithm of linear search."""


def linear_search(doubly_linked_list, target):
    """
    Perform linear search on a doubly linked list to find the target element.
    Args:
        doubly_linked_list: The doubly linked list to search in.
        target: The element to search for.
    Returns:
        True if the target element is found, False otherwise.
    """
    current = doubly_linked_list.head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    return False
