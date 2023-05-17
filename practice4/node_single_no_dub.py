"""This module implements a singly linked list with no duplicates."""
from node_single_linked import SingleLinkedList, Node


class SingleNoDub(SingleLinkedList):
    """
    Class representing a singly linked list with no duplicates.

    This class extends the functionality of a singly linked list and ensures
    that duplicate elements are not added to the list.
    """

    def append(self, data):
        """
        Append an element to the end of the list, ignoring duplicates.

        Args:
            data: The data of the element to be appended.
        """
        if self.head is None:
            self.head = Node(data)
        elif self.head.data != data:
            current = self.head
            while current.next:
                if current.next.data == data:
                    return
                current = current.next
            new_node = Node(data)
            current.next = new_node

    def insert(self, index, data):
        """
        Insert an element at the specified index, ignoring duplicates.

        Args:
            index: The index at which the element should be inserted.
            data: The data of the element to be inserted.
        """
        if self.head is None or self.head.data != data:
            super().insert(index, data)

    def remove_duplicates(self):
        """
        Remove duplicate elements from the list.

        This method removes all occurrences of duplicate elements from the list,
        keeping only the first occurrence of each element.
        """
        if self.head is None:
            return

        current = self.head
        while current:
            next_distinct = current.next
            while next_distinct and next_distinct.data == current.data:
                next_distinct = next_distinct.next
            current.next = next_distinct
            current = next_distinct
