"""Module with double linked list without duplicates."""


class DoublyLinkedList:
    """
    Class representing a doubly linked list without duplicates.
    """

    class Node:
        """
        Class representing a node in the doubly linked list.
        """

        def __init__(self, data):
            """
            Initialize a new instance of the Node class.
            Args:
                data: The data to be stored in the node.
            """
            self.data = data
            self.next = None
            self.prev = None

        def __repr__(self):
            """
            Get the string representation of the node.
            Returns:
                The string representation of the node.
            """
            return str(self.data)

        def get_data(self):
            """
            Get data from class.
            Returns:
                Data value.
            """
            data = self.data
            return data

    def __init__(self):
        """
        Initialize a new instance of the DoublyLinkedList class.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """
        Check if the doubly linked list is empty.
        Returns:
            True if the doubly linked list is empty, False otherwise.
        """
        return self.size == 0

    def get_size(self):
        """
        Get the size of the doubly linked list.
        Returns:
            The number of elements in the doubly linked list.
        """
        return self.size

    def add(self, element):
        """
        Add an element to the doubly linked list.
        Args:
            element: The element to be added.
        """
        new_node = self.Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                if current.data == element:
                    return  # Skip duplicate elements
                current = current.next
            if current.data == element:
                return  # Skip duplicate elements
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        self.size += 1

    def insert(self, index, element):
        """
        Insert an element at the specified index in the doubly linked list.
        Args:
            index: The index at which the element should be inserted.
            element: The element to be inserted.
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        new_node = self.Node(element)

        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.get_node_at_index(index)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

        self.size += 1

    def sort(self):
        """
        Perform insertion sort on the doubly linked list.
        Args:
            self: The doubly linked list to be sorted.
        """
        if self.is_empty() or self.get_size() == 1:
            return
        sorted_tail = self.head.next
        while sorted_tail is not None:
            current = sorted_tail
            while current.prev is not None and current.prev.data > current.data:
                prev_node = current.prev
                next_node = current.next
                if prev_node.prev is not None:
                    prev_node.prev.next = current
                else:
                    self.head = current
                if next_node is not None:
                    next_node.prev = prev_node
                current.prev = prev_node.prev
                current.next = prev_node
                prev_node.prev = current
                prev_node.next = next_node
                current = prev_node
            sorted_tail = sorted_tail.next

    def remove(self, element):
        """
        Remove an element from the doubly linked list.
        Args:
            element: The element to be removed.
        """
        if self.is_empty():
            return
        if self.head.data == element:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return
        current = self.head
        while current is not None:
            if current.data == element:
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                current.prev.next = current.next
                self.size -= 1
                return
            current = current.next

    def contains(self, element):
        """
        Check if the doubly linked list contains an element.
        Args:
            element: The element to check.
        Returns:
            True if the element is found in the doubly linked list, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == element:
                return True
            current = current.next
        return False

    def get_node_at_index(self, index):
        """
        Get the node at the specified index in the doubly linked list.
        Args:
            index: The index of the node to get.
        Returns:
            The node at the specified index.
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current
