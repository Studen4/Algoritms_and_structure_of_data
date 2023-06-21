"""Module to test algorithms working by pytest module."""
import pytest
from level_1_dataset import BasicDataset
from level_2_dataset import ExtendedDataset
from level_3_dataset import BonusDataset


def add_items_to_dataset(dataset, items):
    """
    Add items to the dataset.
    """
    for item in items:
        dataset.append(item)


class TestBasicDataset:
    """Tests for BasicDataset"""
    def test_len(self):
        """
        Test the length of the BasicDataset.
        """
        dataset = BasicDataset()
        assert len(dataset) == 0

        add_items_to_dataset(dataset, [1, 2, 3])
        assert len(dataset) == 3

    def test_repr(self):
        """
        Test the string representation of the BasicDataset.
        """
        dataset = BasicDataset()
        assert repr(dataset) == "[]"

        add_items_to_dataset(dataset, [1, 2, 3])
        assert repr(dataset) == "[1, 2, 3]"

    def test_getitem(self):
        """
        Test accessing items by index in the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        assert dataset[0] == 1
        assert dataset[1] == 2
        assert dataset[2] == 3

    def test_setitem(self):
        """
        Test setting items by index in the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        dataset[1] = 10
        assert dataset[1] == 10

    def test_delitem(self):
        """
        Test deleting items by index in the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        del dataset[1]
        assert len(dataset) == 2
        assert dataset[0] == 1
        assert dataset[1] == 3

    def test_append(self):
        """
        Test appending items to the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        assert len(dataset) == 3
        assert dataset[0] == 1
        assert dataset[1] == 2
        assert dataset[2] == 3

    def test_insert(self):
        """
        Test inserting items into the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        dataset.insert(1, 10)
        assert len(dataset) == 4
        assert dataset[0] == 1
        assert dataset[1] == 10
        assert dataset[2] == 2
        assert dataset[3] == 3

    def test_index(self):
        """
        Test finding the index of an item in the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        assert dataset.index(2) == 1

    def test_remove(self):
        """
        Test removing an item from the BasicDataset.
        """
        dataset = BasicDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        dataset.remove(2)
        assert len(dataset) == 2
        assert dataset[0] == 1
        assert dataset[1] == 3


class TestExtendedDataset:
    """Tests for ExtendedDataset"""
    def test_iter(self):
        """
        Test iterating over the ExtendedDataset.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        items = list(dataset)
        assert items == [1, 2, 3]

    def test_delitem(self):
        """
        Test deleting items by index in the ExtendedDataset.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        del dataset[1]
        assert len(dataset) == 2
        assert dataset[0] == 1
        assert dataset[1] == 3

    def test_clear(self):
        """
        Test clearing the ExtendedDataset.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        dataset.clear()
        assert len(dataset) == 0

    def test_copy(self):
        """
        Test making a copy of the ExtendedDataset.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        new_dataset = dataset.copy()
        assert new_dataset != dataset
        assert len(new_dataset) == len(dataset)
        assert new_dataset[0] == dataset[0]
        assert new_dataset[1] == dataset[1]
        assert new_dataset[2] == dataset[2]

    def test_extend(self):
        """
        Test extending the ExtendedDataset with another dataset or iterable.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2])

        dataset.extend([3, 4])
        assert len(dataset) == 4
        assert dataset[0] == 1
        assert dataset[1] == 2
        assert dataset[2] == 3
        assert dataset[3] == 4

    def test_pop(self):
        """
        Test popping an item from the ExtendedDataset by index.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        item = dataset.pop(1)
        assert len(dataset) == 2
        assert item == 2
        assert dataset[0] == 1
        assert dataset[1] == 3

    def test_reverse(self):
        """
        Test reversing the order of items in the ExtendedDataset.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3])

        dataset.reverse()
        assert len(dataset) == 3
        assert dataset[0] == 3
        assert dataset[1] == 2
        assert dataset[2] == 1

    def test_count(self):
        """
        Test counting the occurrences of an item in the ExtendedDataset.
        """
        dataset = ExtendedDataset()
        add_items_to_dataset(dataset, [1, 2, 3, 2])

        assert dataset.count(2) == 2
        assert dataset.count(4) == 0


class TestBonusDataset:
    """Tests for BonusDataset"""
    def test_add(self):
        """
        Test adding two BonusDatasets together.
        """
        dataset1 = BonusDataset()
        add_items_to_dataset(dataset1, [1, 2])

        dataset2 = BonusDataset()
        add_items_to_dataset(dataset2, [3, 4])

        new_dataset = dataset1 + dataset2
        assert len(new_dataset) == 4
        assert new_dataset[0] == 1
        assert new_dataset[1] == 2
        assert new_dataset[2] == 3
        assert new_dataset[3] == 4

    def test_mul(self):
        """
        Test multiplying a BonusDataset by a scalar.
        """
        dataset = BonusDataset()
        add_items_to_dataset(dataset, [1, 2])

        new_dataset = dataset * 3
        assert len(new_dataset) == 6
        assert new_dataset[0] == 1
        assert new_dataset[1] == 2
        assert new_dataset[2] == 1
        assert new_dataset[3] == 2
        assert new_dataset[4] == 1
        assert new_dataset[5] == 2

    def test_deepcopy(self):
        """
        Test creating a deep copy of the BonusDataset.
        """
        dataset = BonusDataset()
        item1 = [1, 2, 3]
        item2 = [4, 5, 6]
        add_items_to_dataset(dataset, [item1, item2])

        new_dataset = dataset.deepcopy()
        assert new_dataset != dataset
        assert len(new_dataset) == len(dataset)
        assert new_dataset[0] == dataset[0]
        assert new_dataset[1] == dataset[1]
        assert new_dataset[0] == item1
        assert new_dataset[1] == item2

    def test_min(self):
        """
        Test finding the minimum value in the BonusDataset.
        """
        dataset = BonusDataset()
        add_items_to_dataset(dataset, [3, 1, 2])

        assert dataset.min() == 1

    def test_max(self):
        """
        Test finding the maximum value in the BonusDataset.
        """
        dataset = BonusDataset()
        add_items_to_dataset(dataset, [3, 1, 2])

        assert dataset.max() == 3


# Run the tests
if __name__ == "__main__":
    pytest.main()
