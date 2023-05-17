"""Module to init data in Node"""


class Node:
    """Class with node initialization"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """
        Get the data stored in the node.
        Returns:
            The data stored in the node.
        """
        return self.data

    def set_data(self, data):
        """
        Set the data to be stored in the node.
        Args:
            data: The data to be stored in the node.
        """
        self.data = data
