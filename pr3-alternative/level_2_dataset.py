"""Module with extended realisation of dataset."""
from level_1_dataset import BasicDataset


class ExtendedDataset(BasicDataset):
    """Class representing an extended dataset."""

    def __init__(self):
        super().__init__()
        self.current = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        item = self.current.data
        self.current = self.current.next
        return item

    def __delitem__(self, index):
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

    def clear(self):
        """Clear the dataset."""
        self.head = None
        self.tail = None
        self.length = 0

    def copy(self):
        """Return a shallow copy of the dataset."""
        new_dataset = ExtendedDataset()
        for item in self:
            new_dataset.append(item)
        return new_dataset

    def extend(self, items):
        """Extend the dataset by appending items from an iterable."""
        for item in items:
            self.append(item)

    def pop(self, index=-1):
        """Remove and return the item at the specified index in the dataset."""
        if self.length == 0:
            raise IndexError("Pop from empty dataset")
        if index == 0:
            item = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            previous = self._get_node(index - 1)
            current = previous.next
            item = current.data
            previous.next = current.next
            if current.next is None:
                self.tail = previous
        self.length -= 1
        return item

    def reverse(self):
        """Reverse the order of items in the dataset."""
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def count(self, item):
        """Return the number of occurrences of an item in the dataset."""
        count = 0
        current = self.head
        while current:
            if current.data == item:
                count += 1
            current = current.next
        return count
