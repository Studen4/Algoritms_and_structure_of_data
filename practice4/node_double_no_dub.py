"""This module implements a double linked list with no duplicates."""
from node_double_linked import DoubleLinked


class DoubleLinkedNoDub(DoubleLinked):
    """
    Class representing a doubly linked list without duplicates.
    Inherits from DoubleLinked class.
    """

    def append(self, data):
        """
        Append a node with the specified data to the end of the list,
        if it does not already exist in the list.
        Args:
            data: The data to be appended to the list.
        """
        if self.head and self.head.data == data:
            return

        super().append(data)

    def insert(self, index, data):
        """
        Insert a node with the specified data at the specified index in the list,
        if it does not already exist in the list.
        Args:
            index: The index at which to insert the node.
            data: The data to be inserted into the list.
        """
        if self.head and self.head.data == data:
            return

        super().insert(index, data)

    def remove_duplicates(self):
        """
        Remove any duplicate nodes from the list.
        Only the first occurrence of each unique value is retained.
        """
        if not self.head:
            return

        current = self.head
        seen_values = {current.data}
        while current.next:
            if current.next.data in seen_values:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
            else:
                seen_values.add(current.next.data)
                current = current.next
