"""Module with realisation custom list features"""
import copy


class CustomList:
    """Class to create a custom variant of a list"""
    def __init__(self):
        """Initialize an empty custom list"""
        self.size = 0
        self.array = {}

    def __len__(self):
        """Return the number of elements in the custom list"""
        return self.size

    def __repr__(self):
        """Return a string representation of the custom list"""
        return repr([self.array[i] for i in range(self.size)])

    def __getitem__(self, index):
        """Get the element at the specified index"""
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        """Set the element at the specified index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __iter__(self):
        """Return an iterator for the custom list"""
        return iter(self.array)

    def __next__(self):
        """Return the next element from the iterator"""
        raise NotImplementedError

    def __delitem__(self, index):
        """Delete the element at the specified index"""
        del self.array[index]

    def __eq__(self, other):
        """Check if the custom list is equal to another list"""
        if isinstance(other, CustomList):
            return self.array == other.array
        if isinstance(other, list):
            return list(self.array.values()) == other
        return False

    def append(self, value):
        """Append a value to the end of the custom list"""
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """Insert a value at the specified index"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index] = value
        self.size += 1

    def index(self, value):
        """Return the index of the first occurrence of a value"""
        for i in range(self.size):
            if self.array[i] == value:
                return i
        raise ValueError("Value not found")

    def remove(self, value):
        """Remove the first occurrence of a value"""
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j+1]
                del self.array[self.size - 1]
                self.size -= 1
                return
        raise ValueError("Value not found")

    def clear(self):
        """Remove all elements from the custom list"""
        self.array.clear()
        self.size = 0

    def copy(self):
        """Return a shallow copy of the custom list"""
        copied_list = CustomList()
        copied_list.extend(self)
        return copied_list

    def extend(self, other):
        """Extend the custom list by appending elements from another list"""
        if hasattr(other, "__iter__"):
            for item in other:
                self.append(item)
        else:
            raise TypeError("Invalid type for extension. Iterable expected.")

    def reverse(self):
        """Reverse the order of the elements in the custom list"""
        for first_var in range(self.size // 2):
            second_var = self.size - first_var - 1
            self.array[first_var], self.array[second_var] \
                = self.array[second_var], self.array[first_var]

    def count(self, value):
        """Return the number of occurrences of a value in the custom list"""
        count = 0
        for i in range(self.size):
            if self.array[i] == value:
                count += 1
        return count

    def __add__(self, other):
        """Unite two custom lists"""
        if hasattr(other, "__iter__"):
            new_list = CustomList()
            new_list.extend(self)
            new_list.extend(other)
            return new_list
        raise TypeError("Invalid type for extension. CustomList expected.")

    def __mul__(self, other):
        """Multiply the custom list by constant"""
        if isinstance(other, int):
            new_list = CustomList()
            for _ in range(other):
                new_list.extend(self)
            return new_list
        raise TypeError("Invalid type for multiplication. Integer expected.")

    def min(self):
        """Return the minimum value in the custom list"""
        if self.size == 0:
            raise ValueError("List is empty")
        min_value = self.array[0]
        for i in range(1, self.size):
            if self.array[i] < min_value:
                min_value = self.array[i]
        return min_value

    def max(self):
        """Return the maximum value in the custom list"""
        if self.size == 0:
            raise ValueError("List is empty")
        max_value = self.array[0]
        for i in range(1, self.size):
            if self.array[i] > max_value:
                max_value = self.array[i]
        return max_value

    def deepcopy(self):
        """Return a deep copy of the custom list"""
        copied_list = CustomList()
        copied_list.size = self.size
        copied_list.array = copy.deepcopy(self.array)
        return copied_list
