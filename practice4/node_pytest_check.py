"""Module to create 100% test coverage to all functions in all modules"""
from node_part import Node
from node_single_linked import SingleLinkedList
from node_double_linked import DoubleLinked
from node_double_no_dub import DoubleLinkedNoDub
from node_single_no_dub import SingleNoDub
from node_sorted_double import SortedDouble
from node_sorted_single import SortedSingle
from node_sorted_double_no_dub import SortedDoubleNoDub
from node_sorted_single_no_dub import SortedSingleNoDub


def test_node():
    """Function to test node module"""
    node = Node(5)
    assert node.get_data() == 5
    node.set_data(10)
    assert node.get_data() == 10


def test_len():
    """Function to test len in single linked module"""
    lst = SingleLinkedList()
    assert len(lst) == 0
    lst.append(5)
    assert len(lst) == 1
    lst.append(10)
    assert len(lst) == 2


def test_repr():
    """Function to test repr in single linked module"""
    lst = SingleLinkedList()
    assert repr(lst) == '[]'
    lst.append(5)
    assert repr(lst) == '[5]'
    lst.append(10)
    assert repr(lst) == '[5, 10]'


def test_getitem():
    """Function to test getitem in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    assert lst[0] == 5
    assert lst[1] == 10


def test_setitem():
    """Function to test setitem in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst[0] = 15
    lst[1] = 20
    assert lst[0] == 15
    assert lst[1] == 20


def test_iter():
    """Function to test iter in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    result = [x for x in lst]
    assert result == [5, 10, 15]


def test_delitem():
    """Function to test delitem in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    del lst[1]
    assert len(lst) == 2
    assert lst[0] == 5
    assert lst[1] == 15


def test_add():
    """Function to test add in single linked module"""
    lst1 = SingleLinkedList()
    lst1.append(5)
    lst1.append(10)
    lst2 = SingleLinkedList()
    lst2.append(15)
    lst2.append(20)
    lst3 = lst1 + lst2
    assert len(lst3) == 4
    assert lst3[0] == 5
    assert lst3[1] == 10
    assert lst3[2] == 15
    assert lst3[3] == 20


def test_mul():
    """Function to test mul in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst2 = lst * 3
    assert len(lst2) == 6
    assert lst2[0] == 5
    assert lst2[1] == 10
    assert lst2[2] == 5
    assert lst2[3] == 10
    assert lst2[4] == 5
    assert lst2[5] == 10


def test_append():
    """Function to test append in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    assert len(lst) == 1
    assert lst[0] == 5
    lst.append(10)
    assert len(lst) == 2
    assert lst[0] == 5
    assert lst[1] == 10


def test_insert():
    """Function to test insert in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.insert(1, 15)
    assert len(lst) == 3
    assert lst[0] == 5
    assert lst[1] == 15
    assert lst[2] == 10


def test_index():
    """Function to test index in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    assert lst.index(10) == 1


def test_remove():
    """Function to test remove in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    lst.remove(10)
    assert len(lst) == 2
    assert lst[0] == 5
    assert lst[1] == 15


def test_clear():
    """Function to test clear in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.clear()
    assert len(lst) == 0


def test_copy():
    """Function to test copy in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst2 = lst.copy()
    assert len(lst2) == 2
    assert lst2[0] == 5
    assert lst2[1] == 10


def test_extend():
    """Function to test extend in single linked module"""
    lst1 = SingleLinkedList()
    lst1.append(5)
    lst1.append(10)
    lst2 = SingleLinkedList()
    lst2.append(15)
    lst2.append(20)
    lst1.extend(lst2)
    assert len(lst1) == 4
    assert lst1[0] == 5
    assert lst1[1] == 10
    assert lst1[2] == 15
    assert lst1[3] == 20


def test_pop():
    """Function to test pop in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    assert lst.pop() == 15
    assert len(lst) == 2
    assert lst.pop(0) == 5
    assert len(lst) == 1


def test_reverse():
    """Function to test reverse in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    lst.reverse()
    assert len(lst) == 3
    assert lst[0] == 15
    assert lst[1] == 10
    assert lst[2] == 5


def test_count():
    """Function to test count in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(5)
    lst.append(15)
    assert lst.count(5) == 2
    assert lst.count(10) == 1


def test_min():
    """Function to test min in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    assert lst.min() == 5


def test_max():
    """Function to test max in single linked module"""
    lst = SingleLinkedList()
    lst.append(5)
    lst.append(10)
    lst.append(15)
    assert lst.max() == 15


def test_deepcopy():
    """Function to test deepcopy in single linked module"""
    lst = SingleLinkedList()
    lst.append([1, 2, 3])
    lst2 = lst.deepcopy()
    assert lst2[0] == [1, 2, 3]
    lst2[0][0] = 4
    assert lst[0] == [1, 2, 3]


def test_single_linked():
    """Function with all tests for single linked module"""
    test_len()
    test_repr()
    test_getitem()
    test_setitem()
    test_iter()
    test_delitem()
    test_add()
    test_mul()
    test_append()
    test_insert()
    test_index()
    test_remove()
    test_clear()
    test_copy()
    test_extend()
    test_pop()
    test_reverse()
    test_count()
    test_min()
    test_max()
    test_deepcopy()


def test_double_linked():
    """Function to test double linked module"""
    # Test append
    lst = DoubleLinked()
    lst.append(1)
    assert len(lst) == 1
    assert lst.head.data == 1
    assert lst.tail.data == 1
    lst.append(2)
    assert len(lst) == 2
    assert lst.head.data == 1
    assert lst.tail.data == 2
    lst.append(3)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.tail.data == 3

    # Test prepend
    lst = DoubleLinked()
    lst.prepend(3)
    assert len(lst) == 1
    assert lst.head.data == 3
    assert lst.tail.data == 3
    lst.prepend(2)
    assert len(lst) == 2
    assert lst.head.data == 2
    assert lst.tail.data == 3
    lst.prepend(1)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.tail.data == 3

    # Test insert_after
    lst = DoubleLinked()
    lst.append(1)
    node1 = lst.head
    lst.insert_after(node1, 2)
    assert len(lst) == 2
    assert lst.head.data == 1
    assert lst.tail.data == 1
    lst.insert_after(node1, 3)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.tail.data == 1

    # Test remove
    lst = DoubleLinked()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.remove(2)
    assert len(lst) == 2
    assert lst.head.data == 1
    assert lst.tail.data == 3
    lst.remove(1)
    assert len(lst) == 1
    assert lst.head.data == 3
    assert lst.tail.data == 3

    lst.remove(3)
    assert len(lst) == 0
    assert lst.head is None
    assert lst.tail is None


def test_double_linked_no_dub():
    """Function to test double linked module without duplication"""
    # Test append
    lst = DoubleLinkedNoDub()
    lst.append(1)
    assert len(lst) == 1
    assert lst.head.data == 1
    assert lst.tail.data == 1
    lst.append(2)
    assert len(lst) == 2
    assert lst.head.data == 1
    assert lst.tail.data == 2
    lst.append(2)
    assert lst.head.data == 1
    assert lst.tail.data == 2

    # Test insert
    lst = DoubleLinkedNoDub()
    lst.append(1)
    lst.append(2)
    lst.insert(1, 3)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.tail.data == 2
    assert lst.head.next.data == 3
    lst.insert(1, 2)
    assert lst.head.data == 1
    assert lst.tail.data == 2
    assert lst.head.next.data == 2

    # Test remove_duplicates
    lst = DoubleLinkedNoDub()
    lst.append(1)
    lst.append(2)
    lst.append(2)
    lst.append(3)
    lst.remove_duplicates()
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.tail.data == 3
    assert lst.head.next.data == 2
    lst.remove_duplicates()
    assert len(lst) == 3  # No duplicates, list should remain unchanged
    assert lst.head.data == 1
    assert lst.tail.data == 3
    assert lst.head.next.data == 2
    lst.append(2)
    lst.remove_duplicates()
    assert len(lst) == 3  # Duplicate should be removed
    assert lst.head.data == 1
    assert lst.tail.data == 2
    assert lst.head.next.data == 2


def test_single_linked_no_dub():
    """Function to test single linked module without duplication"""
    # Test append
    lst = SingleNoDub()
    lst.append(1)
    assert len(lst) == 1
    assert lst.head.data == 1
    lst.append(2)
    assert len(lst) == 2
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.data == 1
    assert lst.head.next.data == 2

    # Test insert
    lst = SingleNoDub()
    lst.append(1)
    lst.append(2)
    lst.insert(1, 3)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.head.next.data == 3
    assert lst.head.data == 1
    assert lst.head.next.data == 3

    # Test remove_duplicates
    lst = SingleNoDub()
    lst.append(1)
    lst.append(2)
    lst.append(2)
    lst.append(3)
    lst.remove_duplicates()
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    lst.remove_duplicates()
    assert len(lst) == 3  # No duplicates, list should remain unchanged
    assert lst.head.data == 1
    assert lst.head.next.data == 2

    lst.append(2)
    lst.remove_duplicates()
    assert len(lst) == 3  # Duplicate should be removed
    assert lst.head.data == 1
    assert lst.head.next.data == 2


def test_sorted_double():
    """Function to test sorted double linked module"""
    # Test is_ordered
    lst = SortedDouble()
    assert lst.is_ordered() is True
    lst.append(3)
    assert lst.is_ordered() is True
    lst.append(1)
    assert lst.is_ordered() is False
    lst.append(2)
    assert lst.is_ordered() is False

    # Test sort
    lst.sort()
    assert lst.is_ordered() is True
    lst = SortedDouble()
    lst.append(5)
    lst.append(3)
    lst.append(4)
    lst.append(2)
    lst.append(1)
    lst.sort()
    assert lst.is_ordered() is True
    assert len(lst) == 5
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3
    assert lst.head.next.next.next.data == 4
    assert lst.head.next.next.next.next.data == 5

    # Test _merge_sort
    lst = SortedDouble()
    lst.append(5)
    lst.append(3)
    lst.append(4)
    lst.append(2)
    lst.append(1)
    sorted_head = lst._merge_sort(lst.head)
    current = sorted_head
    expected_data = [1, 2, 3, 4, 5]
    for data in expected_data:
        assert current.data == data
        current = current.next

    # Test _get_middle_node
    lst = SortedDouble()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    middle_node = lst._get_middle_node(lst.head)
    assert middle_node.data == 3

    # Test _merge
    left = SortedDouble.Node(1)
    left.next = SortedDouble.Node(3)
    right = SortedDouble.Node(2)
    right.next = SortedDouble.Node(4)
    merged = lst._merge(left, right)
    current = merged
    expected_data = [1, 2, 3, 4]
    for data in expected_data:
        assert current.data == data
        current = current.next


def test_sorted_single():
    """Function to test sorted single linked module"""
    # Test insert_after
    lst = SortedSingle()
    lst.append(1)
    node = lst.head
    lst.insert_after(node, 3)
    lst.insert_after(node, 2)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3

    # Test prepend
    lst = SortedSingle()
    lst.prepend(3)
    lst.prepend(2)
    lst.prepend(1)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3

    # Test append
    lst = SortedSingle()
    lst.append(3)
    lst.append(2)
    lst.append(1)
    assert len(lst) == 3
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3

    # Test insert after tail
    lst = SortedSingle()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    node = lst.head.next.next
    lst.insert_after(node, 4)
    assert len(lst) == 4
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3
    assert lst.head.next.next.next.data == 4


def test_sorted_double_no_dub():
    """Function to test sorted double linked module without duplication"""
    # Test append
    lst = SortedDoubleNoDub()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(2)
    lst.remove_duplicates()
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3

    # Test insert
    lst = SortedDoubleNoDub()
    lst.insert(0, 2)
    lst.insert(0, 1)
    lst.insert(1, 2)
    lst.insert(2, 3)
    lst.insert(2, 2)
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.next.data == 3

    # Test remove_duplicates
    lst = SortedDoubleNoDub()
    lst.append(1)
    lst.append(2)
    lst.append(2)
    lst.append(3)
    lst.append(3)
    lst.append(3)
    lst.remove_duplicates()
    assert lst.head.data == 1
    assert lst.head.next.data == 2
    assert lst.head.next.next.data == 3


def test_sorted_single_no_dub():
    """Function to test sorted single linked module without duplication"""
    # Test append
    lst = SortedSingleNoDub()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(2)
    lst.remove_duplicates()
    assert len(lst) == 3

    # Test insert
    lst = SortedSingleNoDub()
    lst.insert(0, 3)
    lst.insert(0, 2)
    lst.insert(0, 1)
    lst.insert(1, 2)
    lst.remove_duplicates()
    assert len(lst) == 3

    # Test remove_duplicates with no duplicates
    lst = SortedSingleNoDub()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.remove_duplicates()
    assert len(lst) == 3

    # Test remove_duplicates with all duplicates
    lst = SortedSingleNoDub()
    lst.append(1)
    lst.append(1)
    lst.append(1)
    lst.remove_duplicates()
    assert len(lst) == 1

    # Test remove_duplicates with empty list
    lst = SortedSingleNoDub()
    lst.remove_duplicates()
    assert len(lst) == 0


if __name__ == "__main__":
    test_node()
    test_single_linked()
    test_double_linked()
    test_double_linked_no_dub()
    test_single_linked_no_dub()
    test_sorted_double()
    test_sorted_double_no_dub()
    test_single_linked_no_dub()
