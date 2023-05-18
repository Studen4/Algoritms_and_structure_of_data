"""Module to modify CustomList to sorted list mode"""
from lists_with_extra import CustomList


class SortedList(CustomList):
    """Class to sort list values"""
    def append(self, value):
        """Function to correct value append to list"""
        index = 0
        while index < self.size and self.array[index] < value:
            index += 1
        super().insert(index, value)

    def insert(self, index, value):
        """Function to correct value insert to list"""
        raise NotImplementedError("Insert operation not supported in sorted array")

    def search(self, value):
        """Function to search values in list"""
        left = 0
        right = self.size - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == value:
                return mid
            if self.array[mid] < value:
                left = mid + 1
            else:
                right = mid - 1
        return -1
