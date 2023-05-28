"""Module with pytest tree algorithms."""
from mainpart_visual import AbstractTreeBasic, AbstractTreeExtended, AbstractTreeBonus


def test_abstract_tree_basic():
    """Function with all functions test in basic tree realisation"""
    tree = AbstractTreeBasic()
    assert len(tree) == 0
    assert repr(tree) == "BinarySearchTree()"

    tree.insert(5)
    assert len(tree) == 1
    assert repr(tree) == "BinarySearchTree(5)"

    assert tree.find(5) is True
    assert tree.find(10) is False

    tree.remove(5)
    assert len(tree) == 0
    assert repr(tree) == "BinarySearchTree()"


def test_abstract_tree_extended():
    """Function with all functions test in extended tree realisation"""
    tree = AbstractTreeExtended()
    tree.extend([5, 10, 7, 3])

    assert list(tree) == [3, 5, 7, 10]

    assert tree.count(5) == 1
    assert tree.count(8) == 0

    tree.clear()
    assert len(tree) == 0
    assert repr(tree) == "BinarySearchTree()"


def test_abstract_tree_bonus():
    """Function with all functions test in bonus tree realisation"""
    tree1 = AbstractTreeBonus()
    tree1.extend([5, 10, 7, 3])

    tree2 = AbstractTreeBonus()
    tree2.extend([7, 8, 3])

    tree3 = tree1 + tree2
    assert list(tree3) == [3, 3, 5, 7, 7, 8, 10]

    tree4 = tree1 * tree2
    assert list(tree4) == [3, 7]

    assert tree1.max() == 10


if __name__ == "__main__":
    test_abstract_tree_basic()
    test_abstract_tree_extended()
    test_abstract_tree_bonus()
