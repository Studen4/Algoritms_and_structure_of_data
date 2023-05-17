"""Module implementing a deque using a limited linked list."""
from limited_linked_list import LimitedLinkedList


class Deque:
    """
    Class representing a deque (double-ended queue).
    """

    def __init__(self):
        """
        Initialize a new instance of the Deque class.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """
        Check if the deque is empty.
        Returns:
            True if the deque is empty, False otherwise.
        """
        return self.size == 0

    def add_front(self, element):
        """
        Add an element to the front of the deque.
        Args:
            element: The element to be added to the deque.
        """
        new_node = LimitedLinkedList.Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def add_rear(self, element):
        """
        Add an element to the rear of the deque.
        Args:
            element: The element to be added to the deque.
        """
        new_node = LimitedLinkedList.Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_front(self):
        """
        Remove and return the element from the front of the deque.
        Returns:
            The element removed from the front of the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        element = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return element

    def remove_rear(self):
        """
        Remove and return the element from the rear of the deque.
        Returns:
            The element removed from the rear of the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        element = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
        self.size -= 1
        return element

    def peek_front(self):
        """
        Get the element at the front of the deque without removing it.
        Returns:
            The element at the front of the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        return self.head.data

    def peek_rear(self):
        """
        Get the element at the rear of the deque without removing it.
        Returns:
            The element at the rear of the deque, or None if the deque is empty.
        """
        if self.is_empty():
            return None
        return self.tail.data
