"""Module for visualizing tree algorithms."""

from tree_search_by_algorithm import AbstractTreeSearchBy
from tree_bonus_algorithm import AbstractTreeBonus
from tree_extended_algorithm import AbstractTreeExtended
from tree_basic_algorithm import AbstractTreeBasic


def search_by_visual():
    """
    Visualize the search-by algorithm.

    Creates a tree and performs an attribute-based search.
    """
    tree = AbstractTreeSearchBy()

    # Insert elements into the tree
    tree.create_person("John", 25)
    tree.create_person("Jane", 30)
    tree.create_person("Alice", 22)
    tree.create_person("Bob", 35)

    # Perform attribute-based search
    found = tree.find_by("age", 30)
    print("Results of search:")
    for item in found:
        print(item)


def bonus_level_visual():
    """
    Visualize the bonus-level algorithm.

    Creates a tree and performs various operations such as finding the maximum value,
    performing union and intersection with another tree, and traversing the tree.
    """
    tree = AbstractTreeBonus()

    # Insert elements into the tree
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(9)
    tree.insert(6)
    tree.insert(10)
    tree.insert(12)

    # Print maximum value
    print("Maximum value:", tree.max())

    # Perform union with another tree
    other_tree = AbstractTreeBonus()
    other_tree.insert(2)
    other_tree.insert(4)
    other_tree.insert(6)
    other_tree.insert(8)
    union_tree = tree + other_tree
    print("Union of trees:")
    union_tree.traversal()

    # Perform intersection with another tree
    intersection_tree = tree * other_tree
    print("Intersection of trees:")
    intersection_tree.traversal()

    # Perform inorder, preorder, and postorder traversals
    print("Inorder traversal:")
    tree.traversal('inorder')

    print("Preorder traversal:")
    tree.traversal('preorder')

    print("Postorder traversal:")
    tree.traversal('postorder')


def extended_level_visual():
    """
    Visualize the extended-level algorithm.

    Creates a tree and performs operations such as iterating through the tree,
    extending the tree with new values, counting occurrences of a value, and
    replacing values in the tree.
    """
    tree = AbstractTreeExtended()

    # Add values to the tree
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    # Iterate through the tree
    print("Iterating through the tree:")
    for value in tree:
        print(value)

    # Extend the tree with new values
    print('------')
    tree.extend([1, 9, 4])
    for value in tree:
        print(value)

    # Count occurrences of a value
    counter = tree.count(4)
    print("Occurrences of 4:", counter)
    print('------')

    # Replace values in the tree
    tree.replace(4, 6)
    for value in tree:
        print(value)
    print('------')


def basic_level_visual():
    """
    Visualize the basic-level algorithm.

    Creates a tree and performs operations such as finding elements in the tree,
    removing elements from the tree, and printing the tree.
    """
    tree = AbstractTreeBasic()

    # Insert elements into the tree
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(9)
    tree.insert(6)
    tree.insert(10)
    tree.insert(12)

    # Find elements in the tree
    print("Finding elements:")
    print(tree.find(5))  # True
    print(tree.find(8))  # False

    # Remove elements from the tree
    tree.remove(5)
    tree.remove(7)

    # Print the tree
    print("Binary search tree:", tree)


def main():
    """Execute the visualization of tree algorithms."""
    print("=== Search By Algorithm ===")
    search_by_visual()

    print("\n=== Bonus Level Algorithm ===")
    bonus_level_visual()

    print("\n=== Extended Level Algorithm ===")
    extended_level_visual()

    print("\n=== Basic Level Algorithm ===")
    basic_level_visual()


if __name__ == '__main__':
    main()
