"""Module with basic-tree realisation."""
from tree_node import Node


class AbstractTreeBasic:
    """
    Abstract base class for a basic binary search tree.

    Methods:
    - __init__(): Initializes an empty binary search tree.
    - __len__(): Returns the number of elements in the tree.
    - __repr__(): Returns a string representation of the tree.
    - insert(value): Inserts a value into the tree.
    - find(value): Finds the specified value in the tree and returns True if found, False otherwise.
    - remove(value): Removes the specified value from the tree if present.
    - min(): Returns the minimum value in the tree.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        values = []
        self._inorder_traversal(self.root, values.append)
        return f"BinarySearchTree({', '.join(map(str, values))})"

    def insert(self, value):
        """
        Inserts a value into the tree.
        Parameters:
        - value: The value to be inserted.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)
        self.size += 1

    def find(self, value):
        """
        Finds the specified value in the tree and returns True if found, False otherwise.
        Parameters:
        - value: The value to be found.
        Returns:
        - found: True if the value is found, False otherwise.
        """
        return self._find_recursive(value, self.root)

    def remove(self, value):
        """
        Removes the specified value from the tree if present.
        Parameters:
        - value: The value to be removed.
        """
        if self.root is None:
            return
        self.root = self._remove_recursive(value, self.root)
        self.size -= 1

    def min(self):
        """
        Returns the minimum value in the tree.
        Returns:
        - min_value: The minimum value in the tree.
        """
        if self.root is None:
            raise ValueError("The tree is empty.")
        return self._min_recursive(self.root)

    # Private helper methods

    def _insert_recursive(self, value, node):
        """
        Recursively inserts a value into the binary search tree.
        Parameters:
        - value: The value to insert.
        - node: The current node being considered for insertion.
        Returns:
        - None
        """
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)

    def _find_recursive(self, value, node):
        """
        Recursively finds a value in the binary search tree.
        Parameters:
        - value: The value to find.
        - node: The current node being considered for search.
        Returns:
        - found: True if the value is found, False otherwise.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._find_recursive(value, node.left)
        return self._find_recursive(value, node.right)

    def _remove_recursive(self, value, node):
        """
        Recursively removes a value from the binary search tree.
        Parameters:
        - value: The value to remove.
        - node: The current node being considered for removal.
        Returns:
        - node: The updated node structure after removal.
        """
        if node is None:
            return None
        if value < node.value:
            node.left = self._remove_recursive(value, node.left)
        elif value > node.value:
            node.right = self._remove_recursive(value, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_recursive(node.right)
            node.value = successor.value
            node.right = self._remove_recursive(successor.value, node.right)
        return node

    def _min_recursive(self, node):
        """
        Recursively finds the minimum value in the binary search tree.
        Parameters:
        - node: The current node being considered for finding the minimum.
        Returns:
        - node: The node containing the minimum value.
        """
        if node.left is None:
            return node
        return self._min_recursive(node.left)

    def _inorder_traversal(self, node, visit):
        """
        Performs an inorder traversal of the binary search tree.
        Parameters:
        - node: The current node being considered during traversal.
        - visit: A function to be applied to each visited node's value.
        Returns:
        - None
        """
        if node is None:
            return
        self._inorder_traversal(node.left, visit)
        visit(node.value)
        self._inorder_traversal(node.right, visit)
