"""This module implements a double linked list."""
from node_single_linked import SingleLinkedList, Node


class DoubleLinked(SingleLinkedList):
    """Class representing a double linked list."""

    class Node(Node):
        """Class representing a node in a double linked list."""

        def __init__(self, data):
            """
            Initialize a node with the given data.

            Args:
                data: The data to be stored in the node.
            """
            super().__init__(data)
            self.prev = None

    def __init__(self):
        """Initialize an empty double linked list."""
        super().__init__()
        self.tail = None

    def append(self, data):
        """
        Append a node with the given data at the end of the double linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """
        Prepend a node with the given data at the beginning of the double linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, node, data):
        """
        Insert a new node with the given data after the specified node in the double linked list.

        Args:
            node: The node after which the new node should be inserted.
            data: The data to be stored in the new node.
        """
        if node is None:
            return
        new_node = self.Node(data)
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        new_node.prev = node

    def remove(self, value):
        """
        Remove the first node with the given data from the double linked list.
        Args:
            value: The data of the node to be removed.
        """
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                    else:
                        self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
