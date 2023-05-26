"""Module with test algorithms by 500 objects."""
import timeit
import pytest
from basepart_list import MyList
from sort_algorithm_bubble import bubble_sort
from sort_algorithm_insertion import insertion_sort
from sort_algorithm_selection import selection_sort
from sort_algorithm_merge import merge_sort_top_down
from sort_algorithm_quick import quick_sort_recursive
from sort_by_algorithm_bubble import bubble_sort_with_cycles
from sort_by_algorithm_merge import merge_sort_top_down_by_value
from sort_by_algorithm_quick import quick_sort_iterative


def test_sort_algorithm():
    """
    Performs the sort algorithm test using MyList with 10,000 elements.
    """
    my_list = MyList()
    for i in range(500, 0, -1):
        my_list.append(i)

    start_time = timeit.default_timer()
    bubble_sort(my_list)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("\nBubble Sort Execution Time:", execution_time)

    start_time = timeit.default_timer()
    insertion_sort(my_list)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("Insertion Sort Execution Time:", execution_time)

    start_time = timeit.default_timer()
    selection_sort(my_list)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("Selection Sort Execution Time:", execution_time)

    start_time = timeit.default_timer()
    merge_sort_top_down(my_list)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("Merge Sort (Top-Down) Execution Time:", execution_time)

    start_time = timeit.default_timer()
    quick_sort_recursive(my_list)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("Quick Sort (Recursive) Execution Time:", execution_time)


def test_sort_by_algorithm():
    """
    Performs the sort by algorithm test using MyList with 10,000 elements and dictionaries.
    """
    my_list = MyList()
    for i in range(500, 0, -1):
        my_list.append({'name': 'Name ' + str(i), 'age': i})

    # Bubble Sort By Value
    start_time = timeit.default_timer()
    bubble_sort_with_cycles(my_list, get_age())
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("\nBubble Sort By Value Execution Time:", execution_time)

    # Merge Sort (Top-Down) By Value
    start_time = timeit.default_timer()
    merge_sort_top_down_by_value(my_list, get_age())
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("Merge Sort (Top-Down) By Value Execution Time:", execution_time)

    # Quick Sort (Iterative) By Value
    start_time = timeit.default_timer()
    quick_sort_iterative(my_list, get_age())
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    print("Quick Sort (Iterative) By Value Execution Time:", execution_time)


def get_age():
    """
    Helper function to return the 'age' key.
    """
    return 'age'


if __name__ == "__main__":
    pytest.main()
