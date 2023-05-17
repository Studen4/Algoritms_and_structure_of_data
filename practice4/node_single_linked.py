"""This module implements a singly linked list"""
import copy
from node_part import Node


class SingleLinkedList:
    """
    Class representing a singly linked list.
    This class provides the functionality of a singly linked list, allowing
    elements to be appended, inserted, removed, and accessed. It also supports
    various operations such as indexing, iteration, and list manipulation.
    """
    def __init__(self):
        self.head = None
        self.current = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        current = self.head
        repr_str = '['
        while current:
            repr_str += str(current.data)
            if current.next:
                repr_str += ', '
            current = current.next
        repr_str += ']'
        return repr_str

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError('list index out of range')

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError('list index out of range')

        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def __delitem__(self, index):
        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError('list index out of range')

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next

    def __add__(self, other_list):
        """
        Concatenate two lists by creating a new list that contains all elements
        from both lists.
        Args:
            other_list (SingleLinkedList): The list to concatenate.
        Returns:
            A new instance of SingleLinkedList containing elements from both lists.
        """
        new_list = self.copy()
        current = other_list.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def __mul__(self, value):
        """
        Create a new list by concatenating the original list with itself 'n' times.
        Args:
            value (int): The number of times to repeat the list.
        Returns:
            A new instance of SingleLinkedList containing the repeated elements.
        """
        new_list = self.copy()
        for _ in range(value - 1):
            new_list.extend(self)
        return new_list

    def append(self, data):
        """
        Append an element to the end of the list.
        Args:
            data: The element to append.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, index, data):
        """
        Insert an element at the specified index.
        Args:
            index (int): The index at which to insert the element.
            data: The element to insert.
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0:
            index = len(self) + index
        if index < 0 or index > len(self):
            raise IndexError('list index out of range')

        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def index(self, value):
        """
        Get the index of the first occurrence of the specified value.
            Args:
                value: The value to search for.
            Returns:
                The index of the first occurrence of the value.
            Raises:
                ValueError: If the value is not found in the list.
        """
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        raise ValueError(f'{value} is not in list')

    def remove(self, value):
        """
        Remove the first occurrence of the specified value from the list.
        Args:
            value: The value to remove.
        Raises:
            ValueError: If the value is not found in the list.
        """
        if not self.head:
            raise ValueError(f'{value} is not in list')

        if self.head.data == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == value:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError(f'{value} is not in list')

    def clear(self):
        """
        Clear the list by removing all elements.
        """
        self.head = None

    def copy(self):
        """
        Create a shallow copy of the list.
        Returns:
            A new instance of SingleLinkedList with the same elements as the original list.
        """
        new_list = SingleLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list

    def extend(self, other_list):
        """
        Extend the list by appending all elements from another list.

        Args:
            other_list (SingleLinkedList): The list to extend from.
        """
        current = self.head
        while current.next:
            current = current.next
        other_current = other_list.head
        while other_current:
            current.next = Node(other_current.data)
            current = current.next
            other_current = other_current.next

    def pop(self, index=None):
        """
        Remove and return the element at the specified index.

        If no index is specified, the last element is removed and returned.

        Args:
            index (int, optional): The index of the element to remove.

        Returns:
            The removed element.

        Raises:
            IndexError: If the index is out of range.
        """
        if index is None:
            index = len(self) - 1
        if index < 0:
            index = len(self) + index
        if index < 0 or index >= len(self):
            raise IndexError('list index out of range')

        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        current = self.head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        return data

    def reverse(self):
        """
        Reverse the order of elements in the list.
        """
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def count(self, value):
        """
        Count the number of occurrences of the specified value in the list.
        Args:
            value: The value to count.
        Returns:
            The number of occurrences of the value.
        """
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    def min(self):
        """
        Find the minimum element in the list.
        Returns:
            The minimum element.
        Raises:
            ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("List is empty")
        current = self.head
        min_value = current.data
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

    def max(self):
        """
        Find the maximum element in the list.
        Returns:
            The maximum element.
        Raises:
            ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("List is empty")
        current = self.head
        max_value = current.data
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def deepcopy(self):
        """
        Create a deep copy of the list.
        Returns:
            A new instance of SingleLinkedList with the same elements as the original list,
            but with separate Node objects.
        """
        new_list = SingleLinkedList()
        current = self.head
        while current:
            new_list.append(copy.deepcopy(current.data))
            current = current.next
        return new_list
