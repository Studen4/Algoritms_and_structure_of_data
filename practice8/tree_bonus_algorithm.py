"""Module with bonus-tree realisation."""
from tree_extended_algorithm import AbstractTreeExtended


class AbstractTreeBonus(AbstractTreeExtended):
    """
    Bonus binary search tree that inherits from AbstractTreeExtended.

    Methods:
    - max(): Returns the maximum value in the tree.
    - __add__(other): Returns a new tree that is the union
    of the current tree and another tree.
    - __mul__(other): Returns a new tree that contains the intersection
    of the current tree and another tree.
    - traversal(): Prints the values in the tree using a specific traversal order.
    """

    def max(self):
        """
        Returns the maximum value in the tree.
        Returns:
        - maximum: The maximum value in the tree.
        """
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    def __add__(self, other):
        """
        Returns a new tree that is the union of the current tree and another tree.
        Parameters:
        - other: Another tree to be added.
        Returns:
        - result: A new tree that contains the union of the current tree and the other tree.
        """
        result = AbstractTreeBonus()
        result.extend(self)
        result.extend(other)
        return result

    def __mul__(self, other):
        """
        Returns a new tree that contains the intersection of the current tree and another tree.
        Parameters:
        - other: Another tree to be multiplied.
        Returns:
        - result: A new tree that contains the intersection of the current tree and the other tree.
        """
        result = AbstractTreeBonus()
        for value in self:
            if other.count(value) > 0:
                result.insert(value)
        return result

    def _preorder_traversal(self, node, visit):
        """
        Perform a preorder traversal of the tree rooted at the given node.
        Args:
            node: The root node of the current subtree.
            visit: A function to be applied to each visited node.
        Returns:
             None
        """
        if node is not None:
            visit(node.value)
            self._preorder_traversal(node.left, visit)
            self._preorder_traversal(node.right, visit)

    def _postorder_traversal(self, node, visit):
        """
        Perform a postorder traversal of the tree rooted at the given node.
        Args:
             node: The root node of the current subtree.
             visit: A function to be applied to each visited node.
        Returns:
            None
        """
        if node is not None:
            self._postorder_traversal(node.left, visit)
            self._postorder_traversal(node.right, visit)
            visit(node.value)

    def traversal(self, order='inorder'):
        """
        Prints the values in the tree using a specific traversal order.
        Parameters:
        - order: The traversal order ('inorder', 'preorder', 'postorder').
        Returns:
        - None
        """
        if order == 'inorder':
            self._inorder_traversal(self.root, self._visit_print)
        elif order == 'preorder':
            self._preorder_traversal(self.root, self._visit_print)
        elif order == 'postorder':
            self._postorder_traversal(self.root, self._visit_print)

    @staticmethod
    def _visit_print(value):
        print(value)
