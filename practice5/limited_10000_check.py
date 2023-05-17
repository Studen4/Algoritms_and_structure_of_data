"""
Module for performance testing of LimitedStack, Queue, and Deque.

This module contains functions to measure the performance of LimitedStack,
Queue, and Deque data structures
by adding and removing 10,000 elements.

"""

import timeit
from limited_stack import LimitedStack
from limited_queue import Queue
from limited_deque import Deque


def test_stack_performance():
    """
    Measure the performance of the LimitedStack
    data structure by adding and removing 10,000 elements.
    Prints the execution time for push and pop operations.
    """
    stack = LimitedStack()
    elements = list(range(10000))

    def push_elements():
        """
        Helper function to push elements into the stack.
        """
        for element in elements:
            stack.push(element)

    def pop_elements():
        """
        Helper function to pop elements from the stack.
        """
        for _ in range(len(elements)):
            stack.pop()

    push_time = timeit.timeit(push_elements, number=1)
    print(f"Stack push time: {push_time} seconds")

    pop_time = timeit.timeit(pop_elements, number=1)
    print(f"Stack pop time: {pop_time} seconds")


def test_queue_performance():
    """
    Measure the performance of the Queue data structure by adding and removing 10,000 elements.
    Prints the execution time for enqueue and dequeue operations.
    """
    queue = Queue()
    elements = list(range(10000))

    def enqueue_elements():
        """
        Helper function to enqueue elements into the queue.
        """
        for element in elements:
            queue.enqueue(element)

    def dequeue_elements():
        """
        Helper function to dequeue elements from the queue.
        """
        for _ in range(len(elements)):
            queue.dequeue()

    enqueue_time = timeit.timeit(enqueue_elements, number=1)
    print(f"Queue enqueue time: {enqueue_time} seconds")

    dequeue_time = timeit.timeit(dequeue_elements, number=1)
    print(f"Queue dequeue time: {dequeue_time} seconds")


def test_deque_performance():
    """
    Measure the performance of the Deque data structure by adding and removing 10,000 elements.
    Prints the execution time for add_rear and remove_front operations.
    """
    deque = Deque()
    elements = list(range(10000))

    def add_elements():
        """
        Helper function to add elements to the rear of the deque.
        """
        for element in elements:
            deque.add_rear(element)

    def remove_elements():
        """
        Helper function to remove elements from the front of the deque.
        """
        for _ in range(len(elements)):
            deque.remove_front()

    add_time = timeit.timeit(add_elements, number=1)
    print(f"Deque add time: {add_time} seconds")

    remove_time = timeit.timeit(remove_elements, number=1)
    print(f"Deque remove time: {remove_time} seconds")


if __name__ == "__main__":
    test_stack_performance()
    test_queue_performance()
    test_deque_performance()
