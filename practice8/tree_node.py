"""Module with nodes for tree."""


class Node:
    """
    Node class for the binary search tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def is_leaf(self):
        """
        Checks if the node is a leaf node (has no children).
        Returns:
        - is_leaf: True if the node is a leaf, False otherwise.
        """
        return self.left is None and self.right is None

    def has_children(self):
        """
        Checks if the node has any children.
        Returns:
        - has_children: True if the node has children, False otherwise.
        """
        return self.left is not None or self.right is not None
