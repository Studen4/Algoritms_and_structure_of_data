"""Module with algorithm of binary loop search."""


def binary_search(doubly_linked_list, target):
    """
    Perform binary search on a sorted doubly linked list to find the target element.
    Args:
        doubly_linked_list: The sorted doubly linked list to search in.
        target: The element to search for.
    Returns:
        True if the target element is found, False otherwise.
    """
    low = 0
    high = doubly_linked_list.get_size() - 1

    while low <= high:
        mid = (low + high) // 2
        current = doubly_linked_list.get_node_at_index(mid)

        if current.data == target:
            return True
        if current.data < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
