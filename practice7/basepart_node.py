"""Base part module to rewrite data in nodes."""


class Node:
    """Node class for the linked list."""
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        """
        Get the value of the node.
        Returns:
            The value of the node.
        """
        return self.value

    def set_value(self, value):
        """
        Set the value of the node.
        Args:
            value: The new value for the node.
        """
        self.value = value
