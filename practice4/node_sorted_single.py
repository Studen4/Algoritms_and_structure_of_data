"""This module implements a sorted singly linked list."""

from node_single_linked import SingleLinkedList, Node


class SortedSingle(SingleLinkedList):
    """Class representing a sorted singly linked list."""

    def __init__(self):
        super().__init__()
        self.tail = None

    def insert_after(self, node, data):
        """
        Insert a new node with the given data after the specified node.

        Args:
            node (Node): The node after which the new node will be inserted.
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        if self.tail == node:
            self.tail = new_node

    def prepend(self, data):
        """
        Insert a new node with the given data at the beginning of the list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        """
        Insert a new node with the given data in the sorted position in the list.

        Args:
            data: The data to be stored in the new node.
        """
        if not self.head or data < self.head.data:
            self.prepend(data)
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            self.insert_after(current, data)
