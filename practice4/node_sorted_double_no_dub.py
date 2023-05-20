"""This module implements a sorted doubly linked list."""

from node_sorted_double import SortedDouble


class SortedDoubleNoDub(SortedDouble):
    """Class representing a sorted doubly linked list with no duplicates."""

    def append(self, data):
        """
        Append a new node with the given data to the list, if it doesn't already exist.
        Args:
            data: The data to be stored in the new node.
        """
        if self.head and self.head.data == data:
            return

        super().append(data)

    def insert(self, index, data):
        """
        Insert a new node with the given data at the specified index, if it doesn't already exist.
        Args:
            index: The index at which to insert the new node.
            data: The data to be stored in the new node.
        """
        if self.head and self.head.data == data:
            return
        super().insert(index, data)

    def remove_duplicates(self):
        """Remove any duplicate nodes from the list."""
        if not self.head:
            return
        current = self.head
        while current.next:
            if current.data == current.next.data:
                if current.next.next:
                    current.next.next.prev = current
                current.next = current.next.next
            else:
                current = current.next
