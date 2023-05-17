"""This module implements a sorted singly linked list with no duplicates."""

from node_sorted_single import SortedSingle


class SortedSingleNoDub(SortedSingle):
    """Class representing a sorted singly linked list with no duplicates."""

    def __init__(self):
        super().__init__()
        self.tail = None

    def remove_duplicates(self):
        """Remove any duplicate elements from the linked list."""
        if not self.head:
            return

        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
