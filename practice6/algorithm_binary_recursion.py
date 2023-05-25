"""Module with algorithm of binary recursion search."""


def binary_search_recursive(doubly_linked_list, target):
    """
    Perform binary search on a sorted doubly linked list to find the target element using recursion.
    Args:
        doubly_linked_list: The sorted doubly linked list to search in.
        target: The element to search for.
    Returns:
        True if the target element is found, False otherwise.
    """
    def search_recursive(low, high):
        if low > high:
            return False

        mid = (low + high) // 2
        current = doubly_linked_list.get_node_at_index(mid)

        if current.data == target:
            return True
        if current.data < target:
            return search_recursive(mid + 1, high)
        return search_recursive(low, mid - 1)

    return search_recursive(0, doubly_linked_list.get_size() - 1)
