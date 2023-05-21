"""Module defining the Massive class."""


class Massive:
    """
    A dynamic array data structure.
    Attributes:
        capacity (int): The maximum capacity of the array.
        array (list): The underlying array that stores the elements.
        size (int): The number of elements currently stored in the array.

    """

    def __init__(self):
        self.capacity = 16
        self.array = self._create_array(self.capacity)
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr(self.array[:self.size])

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def append(self, value):
        """
        Append the given value to the end of the array.
        If the array reaches its capacity, it is resized to double its current capacity.
        Args:
            value (Any): The value to append to the array.
        """
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """
        Insert the given value at the specified index.
        If the array reaches its capacity, it is resized to double its current capacity.
        Args:
            index (int): The index at which to insert the value.
            value (Any): The value to insert.
        Raises:
            IndexError: If the index is out of range.

        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def index(self, value):
        """
        Find the index of the first occurrence of the given value in the array.
        Args:
            value (Any): The value to search for.
        Returns:
            int: The index of the first occurrence of the value.
        Raises:
            ValueError: If the value is not found in the array.
        """
        for i in range(self.size):
            if self.array[i] == value:
                return i
        raise ValueError("Value not found in the array")

    def remove(self, value):
        """
        Remove the first occurrence of the given value from the array.
        If the array size becomes less than one-fourth of the capacity after removal,
        it is resized to half its current capacity.
        Args:
            value (Any): The value to remove from the array.
        Raises:
            ValueError: If the value is not found in the array.
        """
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                self.array[self.size] = None
                if self.size < self.capacity // 4:
                    self._resize(self.capacity // 2)
                return
        raise ValueError("Value not found in the array")

    @staticmethod
    def _create_array(capacity):
        """
        Create a new array with the specified capacity.
        Args:
            capacity (int): The capacity of the array.
        Returns:
            list: The newly created array.
        """
        return [None] * capacity

    def _resize(self, new_capacity):
        """
        Resize the array to the new capacity.
        Args:
            new_capacity (int): The new capacity of the array.
        """
        new_array = self._create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
