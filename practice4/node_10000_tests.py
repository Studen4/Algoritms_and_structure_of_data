"""Module to generate lists with 10,000 elements"""
import random
import time
from node_single_linked import SingleLinkedList
from node_double_linked import DoubleLinked
from node_double_no_dub import DoubleLinkedNoDub
from node_single_no_dub import SingleNoDub
from node_sorted_double import SortedDouble
from node_sorted_single import SortedSingle
from node_sorted_double_no_dub import SortedDoubleNoDub
from node_sorted_single_no_dub import SortedSingleNoDub


def test_single_linked():
    """Test Single Linked List with 10,000 elements."""
    lst = SingleLinkedList()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Single Linked List - Execution time: {execution_time} seconds")


def test_double_linked():
    """Test Double Linked List with 10,000 elements."""
    lst = DoubleLinked()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Double Linked List - Execution time: {execution_time} seconds")


def test_double_linked_no_dub():
    """Test Double Linked List (No Duplicates) with 10,000 elements."""
    lst = DoubleLinkedNoDub()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Double Linked List (No Duplicates) - Execution time: {execution_time} seconds")


def test_single_no_dub():
    """Test Single Linked List (No Duplicates) with 10,000 elements."""
    lst = SingleNoDub()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Single Linked List (No Duplicates) - Execution time: {execution_time} seconds")


def test_sorted_double():
    """Test Sorted Double Linked List with 10,000 elements."""
    lst = SortedDouble()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Sorted Double Linked List - Execution time: {execution_time} seconds")


def test_sorted_single():
    """Test Sorted Single Linked List with 10,000 elements."""
    lst = SortedSingle()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Sorted Single Linked List - Execution time: {execution_time} seconds")


def test_sorted_double_no_dub():
    """Test Sorted Double Linked List (No Duplicates) with 10,000 elements."""
    lst = SortedDoubleNoDub()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Sorted Double Linked List (No Duplicates) - Execution time: {execution_time} seconds")


def test_sorted_single_no_dub():
    """Test Sorted Single Linked List (No Duplicates) with 10,000 elements."""
    lst = SortedSingleNoDub()
    elements = list(range(10000))
    random.shuffle(elements)

    start_time = time.time()
    for element in elements:
        lst.append(element)
    end_time = time.time()

    assert len(lst) == 10000
    execution_time = end_time - start_time
    print(f"Sorted Single Linked List (No Duplicates) - Execution time: {execution_time} seconds")


if __name__ == "__main__":
    test_single_linked()
    test_double_linked()
    test_double_linked_no_dub()
    test_single_no_dub()
    test_sorted_double()
    test_sorted_single()
    test_sorted_double_no_dub()
    test_sorted_single_no_dub()
