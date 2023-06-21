"""Module which test generation of 10000 elements
 in list and dataset and equal it."""
import timeit
from level_3_dataset import BonusDataset


def add_to_dataset():
    """Dataset generator."""
    dataset = BonusDataset()
    for i in range(10000):
        dataset.append(i)


basic_dataset_time = timeit.timeit(add_to_dataset, number=1)


def add_to_list():
    """List generator."""
    dataset = []
    for i in range(10000):
        dataset.append(i)


list_time = timeit.timeit(add_to_list, number=1)

print("Time for BasicDataset:", basic_dataset_time)
print("Time for list:", list_time)
