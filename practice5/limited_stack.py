"""Module with stack realisation."""
from limited_linked_list import LimitedLinkedList
from limited_massive import Massive


class LimitedStack:
    """
    Implementation of a limited stack data structure using LimitedLinkedList.
    """
    def __init__(self):
        self.stack = LimitedLinkedList()
        self.size = 0

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def push(self, element):
        """
        Pushes an element onto the top of the stack.
        Args:
            element: The element to be pushed onto the stack.
        """
        self.stack.add(element)
        self.size += 1

    def pop(self):
        """
        Removes and returns the top element from the stack.
        Returns:
            The top element of the stack if the stack is not empty, None otherwise.
        """
        if self.is_empty():
            return None
        element = self.get_element_at(self.size - 1)
        self.stack.remove(element)
        self.size -= 1
        return element

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        Returns:
            The top element of the stack if the stack is not empty, None otherwise.
        """
        if self.is_empty():
            return None
        return self.get_element_at(self.size - 1)

    def get_element_at(self, index):
        """
        Returns the element at the specified index in the stack.
        Args:
            index (int): The index of the element to retrieve.
        Returns:
            The element at the specified index if the index is valid, None otherwise.
        """
        if index < 0 or index >= self.size:
            return None
        current = self.stack.head
        for _ in range(index):
            current = current.next
        return current.data


class MassiveStack(LimitedStack):
    """
    Implementation of a stack data structure using a Massive array.
    Inherits from LimitedStack class.
    """
    def __init__(self):
        super().__init__()
        self.array = Massive()
        self.size = 0

    def is_empty(self):
        """
        Checks if the stack is empty.
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def push(self, element):
        """
        Pushes an element onto the top of the stack.
        Args:
            element: The element to be pushed onto the stack.
        """
        self.array.append(element)
        self.size += 1

    def pop(self):
        """
        Removes and returns the top element from the stack.
        Returns:
            The top element of the stack if the stack is not empty, raises an IndexError otherwise.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        self.size -= 1
        element = self.array[self.size]
        self.array[self.size] = None
        return element

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        Returns:
            The top element of the stack if the stack is not empty, raises an IndexError otherwise.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.array[self.size - 1]
