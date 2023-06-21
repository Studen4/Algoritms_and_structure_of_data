"""Module with realisation of practice by list methods"""
import copy


class ListDataset:
    """Class representing a dataset using a list."""

    def __init__(self):
        self.dataset = []
        self.current_index = 0

    def __len__(self):
        return len(self.dataset)

    def __repr__(self):
        return repr(self.dataset)

    def __getitem__(self, index):
        return self.dataset[index]

    def __setitem__(self, index, value):
        self.dataset[index] = value

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.dataset):
            item = self.dataset[self.current_index]
            self.current_index += 1
            return item
        raise StopIteration

    def __delitem__(self, index):
        del self.dataset[index]

    def __add__(self, other):
        new_array = ListDataset()
        new_array.dataset = self.dataset + other.dataset
        return new_array

    def __mul__(self, factor):
        new_array = ListDataset()
        new_array.dataset = self.dataset * factor
        return new_array

    def append(self, item):
        """Add an item to the end of the dataset."""
        self.dataset.append(item)

    def insert(self, index, item):
        """Insert an item at the specified index in the dataset."""
        self.dataset.insert(index, item)

    def index(self, item):
        """Return the index of the first occurrence of an item in the dataset."""
        return self.dataset.index(item)

    def remove(self, item):
        """Remove the first occurrence of an item from the dataset."""
        self.dataset.remove(item)

    def clear(self):
        """Remove all items from the dataset."""
        self.dataset = []

    def copy(self):
        """Return a shallow copy of the dataset."""
        return self.dataset[:]

    def extend(self, items):
        """Extend the dataset by appending multiple items."""
        self.dataset.extend(items)

    def pop(self, index=-1):
        """Remove and return the item at the specified index in the dataset."""
        return self.dataset.pop(index)

    def reverse(self):
        """Reverse the order of items in the dataset."""
        self.dataset.reverse()

    def count(self, item):
        """Return the number of occurrences of an item in the dataset."""
        return self.dataset.count(item)

    def deepcopy(self):
        """Return a deep copy of the dataset."""
        new_dataset = ListDataset()
        new_dataset.dataset = copy.deepcopy(self.dataset)
        return new_dataset
