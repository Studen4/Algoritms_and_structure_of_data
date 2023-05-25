"""Module with test of find algorithms in 10000 objects."""
import timeit
from search_double_linked_list import DoublyLinkedList
from algorithm_linear import linear_search
from algorithm_transition_search import jump_search
from algorithm_binary_loop import binary_search
from algorithm_binary_recursion import binary_search_recursive
from algorithm_fibonacci_search import fibonacci_search
from algorithm_exponential_search import exponential_search


def linear_search_time(doubly_linked_list, target):
    """Measure the execution time of linear search."""
    start_time = timeit.default_timer()
    result = linear_search(doubly_linked_list, target)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


def jump_search_time(doubly_linked_list, target):
    """Measure the execution time of jump search."""
    start_time = timeit.default_timer()
    result = jump_search(doubly_linked_list, target)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


def binary_search_time(doubly_linked_list, target):
    """Measure the execution time of binary search."""
    start_time = timeit.default_timer()
    result = binary_search(doubly_linked_list, target)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


def binary_search_recursive_time(doubly_linked_list, target):
    """Measure the execution time of binary search (recursive)."""
    start_time = timeit.default_timer()
    result = binary_search_recursive(doubly_linked_list, target)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


def fibonacci_search_time(doubly_linked_list, target):
    """Measure the execution time of Fibonacci search."""
    start_time = timeit.default_timer()
    result = fibonacci_search(doubly_linked_list, target)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


def exponential_search_time(doubly_linked_list, target):
    """Measure the execution time of exponential search."""
    start_time = timeit.default_timer()
    result = exponential_search(doubly_linked_list, target)
    if str(result) == str(target):
        result = True
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return result, execution_time


def run_search_algorithms():
    """Create a doubly linked list with 10000 elements"""
    doubly_linked_list = DoublyLinkedList()
    for i in range(1, 10001):
        doubly_linked_list.add(i)

    target = 9999

    linear_result, linear_time = linear_search_time(doubly_linked_list, target)
    jump_result, jump_time = jump_search_time(doubly_linked_list, target)
    binary_result, binary_time = binary_search_time(doubly_linked_list, target)
    recursive_result, recursive_time = binary_search_recursive_time(doubly_linked_list, target)
    fibonacci_result, fibonacci_time = fibonacci_search_time(doubly_linked_list, target)
    exponential_result, exponential_time = exponential_search_time(doubly_linked_list, target)

    print("Linear Search:")
    print("Result:", linear_result)
    print("Execution Time:", linear_time)

    print("Jump Search:")
    print("Result:", jump_result)
    print("Execution Time:", jump_time)

    print("Binary Search:")
    print("Result:", binary_result)
    print("Execution Time:", binary_time)

    print("Recursive Binary Search:")
    print("Result:", recursive_result)
    print("Execution Time:", recursive_time)

    print("Fibonacci Search:")
    print("Result:", fibonacci_result)
    print("Execution Time:", fibonacci_time)

    print("Exponential Search:")
    print("Result:", exponential_result)
    print("Execution Time:", exponential_time)


run_search_algorithms()
