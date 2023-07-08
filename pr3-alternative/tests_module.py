"""Module with visual part of program."""
from dataset_sorted import SortedDataset
from dataset_no_dublication import NoDuplicationDataset
from dataset_by_list import ListDataset
from level_1_dataset import BasicDataset
from level_2_dataset import ExtendedDataset
from level_3_dataset import BonusDataset


def list_dataset_test():
    """Display work of functions in dataset_by_list module."""
    print("Test 1 >>>")
    # Example usage
    dataset = ListDataset()
    dataset.extend([1, 2, 3, 4, 5])
    print("Dataset:", dataset)
    # Iterate over the dataset
    print("Iterating over the dataset:")
    for item in dataset:
        print(item)
    # Add items to the dataset
    dataset.append(6)
    dataset.insert(0, 0)
    print("Updated Dataset:", dataset)
    # Remove items from the dataset
    dataset.remove(3)
    print("Dataset after removing 3:", dataset)
    # Get the index of an item in the dataset
    index = dataset.index(4)
    print("Index of 4:", index)
    # Make a copy of the dataset
    dataset_copy = dataset.copy()
    print("Copy of the dataset:", dataset_copy)
    # Reverse the dataset
    dataset.reverse()
    print("Reversed Dataset:", dataset)
    # Clear the dataset
    dataset.clear()
    print("Cleared Dataset:", dataset)


def basic_dataset_test():
    """Display work of methods in BasicDataset class."""
    print("Test 2 >>>")
    dataset = BasicDataset()
    dataset.append(1)
    dataset.append(2)
    dataset.insert(0, 0)
    print("Dataset:", dataset)
    print("Length of the dataset:", len(dataset))
    item = dataset[1]
    print("Item at index 1:", item)
    dataset[2] = 3
    print("Updated dataset:", dataset)
    try:
        index = dataset.index(2)
        print("Index of 2:", index)
    except ValueError:
        print("Not in dataset!")
    dataset.remove(1)
    print("Dataset after removing 1:", dataset)


def extended_dataset_test():
    """Display work of methods in ExtendedDataset class."""
    print("Test 3 >>>")
    dataset = ExtendedDataset()
    dataset.extend([1, 2, 3, 4, 5])
    print("Dataset:", dataset)
    print("Length of the dataset:", len(dataset))
    item = dataset[1]
    print("Item at index 1:", item)
    dataset[2] = 3
    print("Updated dataset:", dataset)
    index = dataset.index(2)
    print("Index of 2:", index)
    dataset.remove(1)
    print("Dataset after removing 1:", dataset)
    dataset.reverse()
    print("Reversed dataset:", dataset)
    for item in dataset:
        print(item)
    del dataset[0]
    print("Dataset after deleting item at index 0:", dataset)
    dataset.clear()
    print("Cleared dataset:", dataset)


def bonus_dataset_test():
    """Display work of methods in BonusDataset class."""
    print("Test 4 >>>")
    dataset = BonusDataset()
    dataset.extend([1, 2, 3, 4, 5])
    print("Dataset:", dataset)
    print("Length of the dataset:", len(dataset))
    item = dataset[1]
    print("Item at index 1:", item)
    dataset[2] = 3
    print("Updated dataset:", dataset)
    index = dataset.index(2)
    print("Index of 2:", index)
    dataset.remove(1)
    print("Dataset after removing 1:", dataset)
    dataset.reverse()
    print("Reversed dataset:", dataset)
    for item in dataset:
        print(item)
    del dataset[0]
    print("Dataset after deleting item at index 0:", dataset)
    dataset_copy = dataset.copy()
    print("Copy of the dataset:", dataset_copy)
    dataset.clear()
    print("Cleared dataset:", dataset)
    dataset.extend([1, 2, 3])
    dataset2 = BonusDataset()
    dataset2.extend([4, 5, 6])
    dataset3 = dataset + dataset2
    print("Concatenated dataset:", dataset3)
    dataset4 = dataset * 3
    print("Multiplied dataset:", dataset4)
    print("Minimum item:", dataset4.min())
    print("Maximum item:", dataset4.max())
    dataset5 = dataset4.deepcopy()
    print("Deep copy of the dataset:", dataset5)


def no_duplication_dataset_test():
    """Display work of methods in NoDuplicationDataset class."""
    print("Test 5 >>>")
    dataset = NoDuplicationDataset()
    dataset.append(2)
    dataset.append(1)
    dataset.append(3)
    dataset.append(2)
    dataset.append(4)
    dataset.append(1)
    dataset.append(5)
    print("Original dataset:", dataset)
    unique_dataset = dataset.unique()
    print("Dataset without duplicates:", unique_dataset)


def sorted_dataset_test():
    """Display work of methods in SortedDataset class."""
    print("Test 6 >>>")
    dataset = SortedDataset()
    dataset.append(2)
    dataset.append(4)
    dataset.append(6)
    dataset.append(8)
    dataset.append(1)
    dataset.append(3)
    dataset.append(5)
    dataset.append(7)
    dataset.append(9)
    print("Original dataset:", dataset)
    dataset.sort()
    print("Sorted dataset:", dataset)


if __name__ == "__main__":
    list_dataset_test()
    basic_dataset_test()
    extended_dataset_test()
    bonus_dataset_test()
    no_duplication_dataset_test()
    sorted_dataset_test()
