"""Module with basic node class."""


class Node:
    """Class to initialisation and work with node."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """Get the data stored in the node."""
        return self.data

    def set_data(self, new_data):
        """Set the data stored in the node to a new value."""
        self.data = new_data
