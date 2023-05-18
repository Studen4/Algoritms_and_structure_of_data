"""Module which create such logic as list method"""


class List:
    """Class to make some kinds of list"""
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __repr__(self):
        return repr(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def append(self, value):
        """Function to check value and append it to list"""
        self.array.append(value)

    def insert(self, index, value):
        """Function to check index of value and insert it to correct place"""
        self.array.insert(index, value)

    def index(self, value):
        """Function to return index of value"""
        return self.array.index(value)

    def remove(self, value):
        """Function to remove value from list"""
        self.array.remove(value)
