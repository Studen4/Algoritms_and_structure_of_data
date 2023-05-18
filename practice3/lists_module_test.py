"""Module with tests of data lists creations"""
import pytest
from lists_basic import List
from lists_with_extra import CustomList
from lists_without_dublication import UniqueList
from lists_with_sorted_data import SortedList
from generator import Generator


def test_list():
    """Test of basic list"""
    some_list = List()
    some_list.append(1)
    assert len(some_list) == 1
    assert some_list[0] == 1
    some_list[0] = 0
    assert some_list[0] == 0
    some_list.insert(0, 2)
    assert some_list[0] == 2
    assert some_list.index(2) == 0
    some_list.remove(2)
    assert len(some_list) == 1


def test_custom_list():
    """Test of custom list"""
    custom_list = CustomList()
    test_custom_list_generator()
    test_append(custom_list)
    test_index(custom_list)
    test_remove(custom_list)
    test_extend(custom_list)
    test_reverse(custom_list)
    test_min_max(custom_list)
    test_copy(custom_list)
    test_insert(custom_list)
    test_count(custom_list)
    test_multiply(custom_list)
    test_add(custom_list)
    test_clear(custom_list)
    test_exceptions(custom_list)


def test_custom_list_generator():
    """Test of custom list with generator"""
    custom_list = CustomList()
    generator = Generator()
    students = generator.one_thousand_generator()
    for student in students:
        custom_list.append(student)
    assert len(custom_list) == 1000
    assert custom_list[0].name == students[0].name
    custom_list[0] = students[1]
    assert custom_list[0].name == students[1].name
    students_10000 = generator.ten_thousand_generator()
    custom_list_10000 = CustomList()
    for student in students_10000:
        custom_list_10000.append(student)
    for student in students_10000[::-1]:
        custom_list_10000.insert(0, student)
    for student in students_10000:
        custom_list_10000.append(student)
    center_student = custom_list_10000[len(custom_list_10000) // 2]
    for i, _ in enumerate(custom_list_10000):
        custom_list_10000[i] = center_student


def test_append(custom_list):
    """Test append method of custom list"""
    custom_list.append(1)
    assert len(custom_list) == 1
    assert custom_list[0] == 1


def test_index(custom_list):
    """Test index method of custom list"""
    custom_list[0] = 0
    assert custom_list[0] == 0
    custom_list.insert(0, 2)
    assert custom_list[0] == 2
    assert custom_list.index(2) == 0


def test_remove(custom_list):
    """Test remove method of custom list"""
    custom_list.remove(2)
    assert len(custom_list) == 1


def test_extend(custom_list):
    """Test extend method of custom list"""
    custom_list.extend([4, 5, 6])
    assert len(custom_list) == 4
    assert custom_list[-1] == 6


def test_reverse(custom_list):
    """Test reverse method of custom list"""
    custom_list.reverse()
    assert custom_list == [6, 5, 4, 0]


def test_min_max(custom_list):
    """Test min and max methods of custom list"""
    assert custom_list.min() == 0
    assert custom_list.max() == 6


def test_copy(custom_list):
    """Test copy method of custom list"""
    custom_list_copy = custom_list.deepcopy()
    assert custom_list_copy == custom_list
    custom_list_copy.clear()
    assert len(custom_list_copy) == 0
    assert len(custom_list) == 4
    custom_list_copy = custom_list.copy()
    assert list(custom_list_copy) == list(custom_list)


def test_insert(custom_list):
    """Test insert method of custom list"""
    custom_list_copy = custom_list.copy()
    custom_list_copy.insert(0, -1)
    assert custom_list_copy != custom_list
    assert len(custom_list_copy) == 5
    custom_list_copy.remove(-1)
    assert len(custom_list_copy) == 4


def test_count(custom_list):
    """Test count method of custom list"""
    custom_list_mul = custom_list * 3
    assert len(custom_list_mul) == 12
    assert custom_list_mul.count(0) == 3
    assert custom_list_mul.count(6) == 0


def test_multiply(custom_list):
    """Test multiplication operator of custom list"""
    custom_list_mul = custom_list * 3
    assert len(custom_list_mul) == 12
    assert custom_list_mul.count(0) == 3
    assert custom_list_mul.count(6) == 0


def test_add(custom_list):
    """Test addition operator of custom list"""
    custom_list += [7, 8]
    assert len(custom_list) == 6
    assert custom_list[-1] == 8
    assert custom_list.index(7) == 4


def test_clear(custom_list):
    """Test clear method of custom list"""
    custom_list.clear()
    assert len(custom_list) == 0


def test_exceptions(custom_list):
    """Test exceptions raised by custom list"""
    with pytest.raises(IndexError):
        custom_list[0] = 1
        custom_list.insert(1, 2)
        custom_list.remove(3)
        custom_list.reverse()
    with pytest.raises(ValueError):
        custom_list.remove(1)
        custom_list.min()
        custom_list.max()


def test_unique_list():
    """Test of unique list"""
    unique_list = UniqueList()
    unique_list.append(1)
    assert len(unique_list) == 1
    assert unique_list[0] == 1
    unique_list.insert(0, 2)
    assert unique_list[0] == 2
    assert unique_list.index(2) == 0
    with pytest.raises(ValueError):
        unique_list.append(1)
    unique_list.remove(2)
    assert len(unique_list) == 1


def test_sorted_list():
    """Test of sorted list"""
    sorted_list = SortedList()
    sorted_list.append(3)
    sorted_list.append(1)
    sorted_list.append(2)
    assert sorted_list[0] == 1
    assert sorted_list.search(2) == 1
    assert sorted_list.search(5) == -1
    with pytest.raises(NotImplementedError):
        sorted_list.insert(1, 4)
