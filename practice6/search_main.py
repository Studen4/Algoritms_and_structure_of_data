"""Main module which display visual of all program."""

from search_double_linked_list import DoublyLinkedList
import algorithm_linear
import algorithm_transition_search
import algorithm_binary_loop
import algorithm_binary_recursion
import algorithm_fibonacci_search
import algorithm_exponential_search


class VisualSearch:
    """Visual part of program."""
    def __init__(self):
        self.doubly_linked_list = DoublyLinkedList()

    def write_linked_list(self):
        """
        Add elements to the doubly linked list.
        """
        self.doubly_linked_list.add(10)
        self.doubly_linked_list.add(20)
        self.doubly_linked_list.add(30)
        self.doubly_linked_list.add(40)
        self.doubly_linked_list.add(50)

    def visual_linear_search(self):
        """
        Perform linear search on the doubly linked list
        and visualize the process.
        """
        self.write_linked_list()

        print(algorithm_linear.linear_search
              (self.doubly_linked_list, 20))  # True
        print(algorithm_linear.linear_search
              (self.doubly_linked_list, 60))

    def visual_transition_search(self):
        """
        Perform jump search on the doubly linked list
        and visualize the process.
        """
        self.write_linked_list()

        print(algorithm_transition_search.jump_search
              (self.doubly_linked_list, 30))  # True
        print(algorithm_transition_search.jump_search
              (self.doubly_linked_list, 35))

    def visual_binary_loop(self):
        """
        Perform binary search (loop) on the doubly linked list
        and visualize the process.
        """
        self.write_linked_list()

        print(algorithm_binary_loop.binary_search
              (self.doubly_linked_list, 30))  # True
        print(algorithm_binary_loop.binary_search
              (self.doubly_linked_list, 35))

    def visual_binary_recursion(self):
        """
        Perform binary search (recursion) on the doubly
        linked list and visualize the process.
        """
        self.write_linked_list()

        print(algorithm_binary_recursion.binary_search_recursive
              (self.doubly_linked_list, 30))  # True
        print(algorithm_binary_recursion.binary_search_recursive
              (self.doubly_linked_list, 35))

    def visual_fibonacci_search(self):
        """
        Perform Fibonacci search on the doubly linked list
        and visualize the process.
        """
        self.write_linked_list()

        print(algorithm_fibonacci_search.fibonacci_search
              (self.doubly_linked_list, 30))  # 2
        print(algorithm_fibonacci_search.fibonacci_search
              (self.doubly_linked_list, 35))  # -1

    def visual_exponential_search(self):
        """
        Perform exponential search on the doubly linked list
        and visualize the process.
        """
        self.write_linked_list()

        algorithm = algorithm_exponential_search

        target = 30
        node = algorithm.exponential_search(self.doubly_linked_list, target)
        if node is not None:
            print(f"Found node with data {node.data} for target {target}")
        else:
            print(f"Node with target {target} not found")

        target = 35
        node = algorithm.exponential_search(self.doubly_linked_list, target)
        if node is not None:
            print(f"Found node with data {node.data} for target {target}")
        else:
            print(f"Node with target {target} not found")


if __name__ == "__main__":
    visual_search = VisualSearch()

    print("\nLinear Search:")
    visual_search.visual_linear_search()

    print("\nTransition Search:")
    visual_search.visual_transition_search()

    print("\nBinary Search (Loop):")
    visual_search.visual_binary_loop()

    print("\nBinary Search (Recursion):")
    visual_search.visual_binary_recursion()

    print("\nFibonacci Search:")
    visual_search.visual_fibonacci_search()

    print("\nExponential Search:")
    visual_search.visual_exponential_search()
