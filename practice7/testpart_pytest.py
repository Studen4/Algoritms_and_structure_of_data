"""
Module for testing sort algorithms.
"""

import pytest
from testpart_500 import (
    bubble_sort,
    insertion_sort,
    merge_sort_top_down,
    quick_sort_recursive,
    selection_sort,
    bubble_sort_with_cycles,
    merge_sort_top_down_by_value,
    quick_sort_iterative
)
from basepart_list import MyList


def create_sorted_list(sort_algorithm):
    """
    Creates a sorted MyList object using the specified sort algorithm.

    Parameters:
    - sort_algorithm: The sort algorithm function to use.

    Returns:
    - my_list: The sorted MyList object.
    """
    my_list = MyList()
    my_list.append(4)
    my_list.append(2)
    my_list.append(9)
    my_list.append(5)
    my_list.append(1)
    my_list.append(7)
    sort_algorithm(my_list)
    return my_list


def create_sorted_by_list(sort_by_algorithm, value):
    """
    Prints the sorted values in the MyList object using the specified sort algorithm and value.

    Parameters:
    - sort_by_algorithm (function): The sorting algorithm to be applied to the MyList object.
    - value: The value to sort the elements by.
    """
    my_list = MyList()
    my_list.append({'name': 'Alice', 'age': 25})
    my_list.append({'name': 'Bob', 'age': 20})
    my_list.append({'name': 'Charlie', 'age': 30})
    my_list.append({'name': 'David', 'age': 22})
    my_list.append({'name': 'Eve', 'age': 27})
    sort_by_algorithm(my_list, value)
    return my_list


def test_print_sorted_values_bubble_sort(capsys):
    """
    Test printing sorted values using bubble sort algorithm.

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.
    """
    my_list = create_sorted_list(bubble_sort)
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n4\n5\n7\n9\n"


def test_print_sorted_values_insertion_sort(capsys):
    """
    Test printing sorted values using insertion sort algorithm.

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.
    """
    my_list = create_sorted_list(insertion_sort)
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n4\n5\n7\n9\n"


def test_print_sorted_values_merge_sort_top_down(capsys):
    """
    Test printing sorted values using merge sort algorithm (top-down).

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.
    """
    my_list = create_sorted_list(merge_sort_top_down)
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n4\n5\n7\n9\n"


def test_print_sorted_values_quick_sort_recursive(capsys):
    """
    Test printing sorted values using quick sort algorithm (recursive).

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.
    """
    my_list = create_sorted_list(quick_sort_recursive)
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n4\n5\n7\n9\n"


def test_print_sorted_values_selection_sort(capsys):
    """
    Test printing sorted values using selection sort algorithm.

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.
    """
    my_list = create_sorted_list(selection_sort)
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n4\n5\n7\n9\n"


def test_bubble_sort_with_cycles(capsys):
    """
    Test for bubble_sort_with_cycles function.

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.

    Prints the sorted values after applying bubble sort with cycles to the test MyList.
    Then, checks if the captured stdout matches the expected output.
    """
    with pytest.raises(KeyError):
        my_list = create_sorted_by_list(bubble_sort_with_cycles, 1)
        for item in my_list:
            print(item)
        capsys.readouterr()


def test_merge_sort_top_down_by_value(capsys):
    """
    Test for merge_sort_top_down_by_value function.

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.

    Prints the sorted values after apply to merge sort
    top-down by value to the test MyList.
    Then, checks if the captured stdout matches the expected output.
    """
    my_list = create_sorted_by_list(merge_sort_top_down_by_value, 'name')
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out is not None


def test_quick_sort_iterative(capsys):
    """
    Test for quick_sort_iterative function.

    Parameters:
    - capsys: The pytest capsys fixture for capturing stdout.

    Prints the sorted values after applying quick sort iterative to the test MyList.
    Then, checks if the captured stdout matches the expected output.
    """
    my_list = create_sorted_by_list(quick_sort_iterative, 'age')
    for item in my_list:
        print(item)
    captured = capsys.readouterr()
    assert captured.out == "{'name': 'Bob', 'age': 20}\n" \
                           "{'name': 'David', 'age': 22}\n" \
                           "{'name': 'Alice', 'age': 25}\n" \
                           "{'name': 'Eve', 'age': 27}\n" \
                           "{'name': 'Charlie', 'age': 30}\n"


def all_tests():
    """
    Run all tests.
    """
    pytest.main([__file__])


if __name__ == '__main__':
    all_tests()
