"""Module to refactor CustomList to list with unique values"""
from lists_with_extra import CustomList


class UniqueList(CustomList):
    """Class to check variables unique and drop duplication variants"""
    def append(self, value):
        """Function to append new unique value to list"""
        if value in self.array.values():
            raise ValueError("Value already exists")
        super().append(value)

    def insert(self, index, value):
        """Function to insert new unique value to list"""
        if value in self.array.values():
            raise ValueError("Value already exists")
        super().insert(index, value)
