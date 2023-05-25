"""Module with pytest for the search algorithms."""

import pytest
import search_main


@pytest.mark.skip
def test_adder(doubly_linked_list):
    """
    Test the adder function of the DoublyLinkedList.
    """
    doubly_linked_list.add(10)
    doubly_linked_list.add(20)
    doubly_linked_list.add(30)


def test_linear_search():
    """
    Test the linear search algorithm.
    """
    doubly_linked_list = search_main.DoublyLinkedList()
    test_adder(doubly_linked_list)
    algorithm = search_main.algorithm_linear
    assert algorithm.linear_search(doubly_linked_list, 10) is True
    assert algorithm.linear_search(doubly_linked_list, 20) is True
    assert algorithm.linear_search(doubly_linked_list, 30) is True
    assert algorithm.linear_search(doubly_linked_list, 40) is False


def test_jump_search():
    """
    Test the jump search algorithm.
    """
    doubly_linked_list = search_main.DoublyLinkedList()
    test_adder(doubly_linked_list)
    algorithm = search_main.algorithm_transition_search
    assert algorithm.jump_search(doubly_linked_list, 10) is True
    assert algorithm.jump_search(doubly_linked_list, 20) is True
    assert algorithm.jump_search(doubly_linked_list, 30) is True
    assert algorithm.jump_search(doubly_linked_list, 40) is False


def test_binary_search():
    """
    Test the binary search algorithm.
    """
    doubly_linked_list = search_main.DoublyLinkedList()
    test_adder(doubly_linked_list)
    algorithm = search_main.algorithm_binary_loop
    assert algorithm.binary_search(doubly_linked_list, 10) is True
    assert algorithm.binary_search(doubly_linked_list, 20) is True
    assert algorithm.binary_search(doubly_linked_list, 30) is True
    assert algorithm.binary_search(doubly_linked_list, 40) is False


def test_binary_search_recursive():
    """
    Test the recursive binary search algorithm.
    """
    doubly_linked_list = search_main.DoublyLinkedList()
    algorithm = search_main.algorithm_binary_recursion
    test_adder(doubly_linked_list)
    assert algorithm.binary_search_recursive(doubly_linked_list, 10) is True
    assert algorithm.binary_search_recursive(doubly_linked_list, 20) is True
    assert algorithm.binary_search_recursive(doubly_linked_list, 30) is True
    assert algorithm.binary_search_recursive(doubly_linked_list, 40) is False


def test_fibonacci_search():
    """
    Test the Fibonacci search algorithm.
    """
    doubly_linked_list = search_main.DoublyLinkedList()
    algorithm = search_main.algorithm_fibonacci_search
    test_adder(doubly_linked_list)
    assert algorithm.fibonacci_search(doubly_linked_list, 1) is False
    assert algorithm.fibonacci_search(doubly_linked_list, 2.5) is False
    assert algorithm.fibonacci_search(doubly_linked_list, 0) is False
    assert algorithm.fibonacci_search(doubly_linked_list, 40) is False


def test_exponential_search():
    """
    Test the exponential search algorithm.
    """
    doubly_linked_list = search_main.DoublyLinkedList()
    algorithm = search_main.algorithm_exponential_search
    test_adder(doubly_linked_list)
    assert algorithm.exponential_search(doubly_linked_list, 10) is not None
    assert algorithm.exponential_search(doubly_linked_list, 20) is not None
    assert algorithm.exponential_search(doubly_linked_list, 30) is not None
    assert algorithm.exponential_search(doubly_linked_list, 40) is None


def all_tests():
    """
    Run all the tests.
    """
    test_linear_search()
    test_jump_search()
    test_binary_search()
    test_binary_search_recursive()
    test_fibonacci_search()
    test_exponential_search()


if __name__ == "__main__":
    all_tests()
