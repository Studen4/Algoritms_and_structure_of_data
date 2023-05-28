"""Module with tree sorting 100.000 elements."""
import random
import time
from tree_basic_algorithm import AbstractTreeBasic


def test_sorting():
    """Generate a list of 100.000 random numbers"""
    numbers = [random.randint(1, 100000) for _ in range(100000)]

    # Create an instance of the binary search tree
    tree = AbstractTreeBasic()

    # Insert the numbers into the tree
    for number in numbers:
        tree.insert(number)

    # Test sorting algorithm
    start_time = time.time()
    sorted_numbers = []
    tree._inorder_traversal(tree.root, sorted_numbers.append)
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time

    # Print the sorted list and execution time
    print("Sorted numbers:", sorted_numbers)
    print("Execution time:", execution_time, "seconds")


if __name__ == "__main__":
    # Run the test
    test_sorting()
