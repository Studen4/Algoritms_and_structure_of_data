"""Base part module with list implementation."""
from basepart_node import Node


class MyList:
    """Custom implementation of a linked list."""
    def __init__(self):
        self.data = None

    def __len__(self):
        count = 0
        current = self.data
        while current is not None:
            count += 1
            current = current.next
        return count

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.data
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.data
        for _ in range(index):
            current = current.next
        current.value = value

    def append(self, item):
        """
        Append an item to the end of the linked list.
        Args:
            item: The item to be appended.
        """
        new_node = Node(item)
        if self.data is None:
            self.data = new_node
        else:
            current = self.data
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get_sublist(self, start, end):
        """
        Returns a new MyList object that contains elements in the specified range.
        Parameters:
        - start (int): The starting index (inclusive) of the sublist.
        - end (int): The ending index (exclusive) of the sublist.
        Returns:
        - MyList: The sublist of elements.
        """
        if start < 0 or end > len(self):
            raise IndexError("Index out of range")
        sublist = MyList()
        current = self.data
        for _ in range(start):
            current = current.next
        for _ in range(start, end):
            sublist.append(current.value)
            current = current.next
        return sublist
