"""Module with algorithm of exponential set search."""


def exponential_search(doubly_linked_list, target):
    """
    Perform exponential search to find the node containing
    the target element in a sorted linked list.
    Args:
        doubly_linked_list: A sorted doubly linked list without duplicates.
        target: The element to search for.
    Returns:
        The node containing the target element if found, otherwise None.
    """
    if doubly_linked_list.is_empty():
        return False

    if doubly_linked_list.head.data == target:
        return True

    # Find the range for binary search
    length = doubly_linked_list.get_size()
    i = 1
    while i < length and doubly_linked_list.get_node_at_index(i).data <= target:
        i *= 2

    return binary_search(doubly_linked_list, target, i // 2, min(i, length - 1))


def binary_search(doubly_linked_list, target, low, high):
    """
    Perform binary search to find the node containing
    the target element in a sorted linked list.
    Args:
        doubly_linked_list: A sorted doubly linked list without duplicates.
        target: The element to search for.
        low: The lower index of the search range.
        high: The upper index of the search range.
    Returns:
        The node containing the target element if found, otherwise None.
    """
    while low <= high:
        mid = (low + high) // 2
        mid_node = doubly_linked_list.get_node_at_index(mid)

        if mid_node.data == target:
            return mid_node
        if mid_node.data < target:
            low = mid + 1
        else:
            high = mid - 1

    return None
