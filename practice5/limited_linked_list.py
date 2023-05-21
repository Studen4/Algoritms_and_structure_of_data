"""Module implementing a limited linked list."""


class LimitedLinkedList:
    """Class representing a limited linked list."""

    class Node:
        """Class representing a node in the linked list."""
        def __init__(self, data):
            """
            Initialize a new instance of the Node class.
            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.next = None

        def __repr__(self):
            """
            Get the string representation of the node.
            Returns:
                The string representation of the node.
            """
            return str(self.data)

        def __str__(self):
            """
            Get the string representation of the node.
            Returns:
                The string representation of the node.
            """
            return str(self.data)

        def get_data(self):
            """
            Get the data stored in the node.
            Returns:
                The data stored in the node.
            """
            return self.data

    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        """
        Get the string representation of the limited linked list.
        Returns:
            The string representation of the limited linked list.
        """
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"

    def is_empty(self):
        """
        Check if the limited linked list is empty.
        Returns:
            True if the limited linked list is empty, False otherwise.
        """
        return self.size == 0

    def get_size(self):
        """
        Get the size of the limited linked list.
        Returns:
            The number of elements in the limited linked list.
        """
        return self.size

    def add(self, element):
        """
        Add an element to the limited linked list.
        Args:
            element: The element to be added.
        """
        new_node = self.Node(element)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, element):
        """
        Remove an element from the limited linked list.
        Args:
            element: The element to be removed.
        """
        if self.head is None:
            return
        if self.head.data == element:
            self.head = self.head.next
            self.size -= 1
            return
        current = self.head
        prev = None
        while current is not None:
            if current.data == element:
                prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def contains(self, element):
        """
        Check if the limited linked list contains an element.
        Args:
            element: The element to check.
        Returns:
            True if the element is found in the limited linked list, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == element:
                return True
            current = current.next
        return False
