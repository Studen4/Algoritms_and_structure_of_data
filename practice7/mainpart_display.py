"""Module with display work of all algorithms."""
from basepart_list import MyList
from sort_algorithm_bubble import bubble_sort
from sort_algorithm_insertion import insertion_sort
from sort_algorithm_selection import selection_sort
from sort_algorithm_merge import merge_sort_top_down
from sort_algorithm_quick import quick_sort_recursive
from sort_by_algorithm_bubble import bubble_sort_with_cycles
from sort_by_algorithm_merge import merge_sort_top_down_by_value
from sort_by_algorithm_quick import quick_sort_iterative


def print_sorted_values(sort_algorithm):
    """Function to append values into MyList"""
    my_list = MyList()
    my_list.append(4)
    my_list.append(2)
    my_list.append(9)
    my_list.append(5)
    my_list.append(1)
    my_list.append(7)
    sort_algorithm(my_list)
    for _, item in enumerate(my_list):
        print(item)


def print_sorted_values_by(sort_by_algorithm, value):
    """Function to append dict values into MyList"""
    my_list = MyList()
    my_list.append({'name': 'Alice', 'age': 25})
    my_list.append({'name': 'Bob', 'age': 20})
    my_list.append({'name': 'Charlie', 'age': 30})
    sort_by_algorithm(my_list, value)
    for _, item in enumerate(my_list):
        print(item)


if __name__ == "__main__":
    # Sort algorithms
    print("Bubble Sort:")
    print_sorted_values(bubble_sort)

    print("\nInsertion Sort:")
    print_sorted_values(insertion_sort)

    print("\nSelection Sort:")
    print_sorted_values(selection_sort)

    print("\nMerge Sort (Top-Down):")
    print_sorted_values(merge_sort_top_down)

    print("\nQuick Sort (Iterative):")
    print_sorted_values(quick_sort_recursive)

    # Sort by algorithms
    print("\nBubble Sort By Value:")
    print_sorted_values_by(bubble_sort_with_cycles, 'age')

    print("\nMerge Sort (Top-Down) By Value:")
    print_sorted_values_by(merge_sort_top_down_by_value, 'age')

    print("\nQuick Sort (Iterative) By Value:")
    print_sorted_values_by(quick_sort_iterative, 'age')
