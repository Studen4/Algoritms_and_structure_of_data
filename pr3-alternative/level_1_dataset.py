"""Module with basic realisation of dataset."""
from struct_node import Node


class BasicDataset:
    """Class representing a basic dataset."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __repr__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

    def __getitem__(self, index):
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        current = self._get_node(index)
        return current.data

    def __setitem__(self, index, value):
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        current = self._get_node(index)
        current.data = value

    def __delitem__(self, index):
        """Delete the item at the specified index in the dataset."""
        if not 0 <= index < self.length:
            raise IndexError("Index out of range")
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            previous = self._get_node(index - 1)
            current = previous.next
            previous.next = current.next
            if current.next is None:
                self.tail = previous
        self.length -= 1

    def append(self, item):
        """Add an item to the end of the dataset."""
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, item):
        """Insert an item at the specified index in the dataset."""
        if not 0 <= index <= self.length:
            raise IndexError("Index out of range")
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            previous = self._get_node(index - 1)
            new_node.next = previous.next
            previous.next = new_node
            if previous == self.tail:
                self.tail = new_node
        self.length += 1

    def index(self, item):
        """Return the index of the first occurrence of an item in the dataset."""
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError("Item not found in the dataset")

    def remove(self, item):
        """Remove the first occurrence of an item from the dataset."""
        index = self.index(item)
        del self[index]

    def _get_node(self, index):
        """Get the node at the specified index in the dataset."""
        current = self.head
        for _ in range(index):
            current = current.next
        return current
