"""Module with extended-tree realisation."""
from tree_basic_algorithm import AbstractTreeBasic


class AbstractTreeExtended(AbstractTreeBasic):
    """
    Extended binary search tree that inherits from AbstractTreeBasic.

    Methods:
    - clear(): Clears the tree.
    - replace(old_value, new_value): Replaces all occurrences
    of old_value with new_value in the tree.
    - __iter__(): Returns an iterator for the tree.
    - __next__(): Returns the next value in the iterator.
    - extend(values): Extends the tree by inserting multiple values.
    - count(value): Counts the number of occurrences of a value in the tree.
    """

    def __init__(self):
        """Initializes the tree."""
        super().__init__()
        self.iterator_values = []
        self.iterator_index = 0

    def __iter__(self):
        self.clear_iterator()
        self._inorder_traversal(self.root, self.iterator_values.append)
        self.iterator_index = 0
        return self

    def __next__(self):
        if self.iterator_index >= len(self.iterator_values):
            raise StopIteration
        values = self.iterator_values[self.iterator_index]
        self.iterator_index += 1
        return values

    def clear_iterator(self):
        """Clears the iterator values."""
        self.iterator_values = []

    def extend(self, values):
        """
        Extends the tree by inserting multiple values.
        Parameters:
        - values: An iterable containing the values to be inserted.
        Returns:
        - None
        """
        for element in values:
            self.insert(element)

    def count(self, values):
        """
        Counts the number of occurrences of a value in the tree.
        Parameters:
        - value: The value to count.
        Returns:
        - occurrence_count: The number of occurrences of the value in the tree.
        """
        occurrence_count = self._count_recursive(values, self.root)
        return occurrence_count

    # Private helper methods

    def _count_recursive(self, values, node):
        """
        Recursively counts the number of occurrences of a value in the tree.
        Parameters:
        - value: The value to count.
        - nodes: The current nodes being considered for counting.
        Returns:
        - count: The count of occurrences.
        """
        if node is None:
            return 0
        count = 0
        if node.value == values:
            count += 1
        count += self._count_recursive(values, node.left)
        count += self._count_recursive(values, node.right)
        return count

    def clear(self):
        """Clears the tree by setting the root to None and the size to 0."""
        self.root = None
        self.size = 0

    def replace(self, old_value, new_value):
        """
        Replaces all occurrences of old_value with new_value in the tree.
        Parameters:
        - old_value: The value to be replaced.
        - new_value: The value to replace with.
        """
        self.remove(old_value)
        self.insert(new_value)
