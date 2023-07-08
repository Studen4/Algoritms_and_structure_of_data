"""Module with bonus realisation of dataset."""
from level_2_dataset import ExtendedDataset
from dataset_by_list import copy


class BonusDataset(ExtendedDataset):
    """Class representing a bonus dataset."""

    def __add__(self, other):
        new_dataset = BonusDataset()
        for item in self:
            new_dataset.append(item)
        for item in other:
            new_dataset.append(item)
        return new_dataset

    def __mul__(self, factor):
        new_dataset = BonusDataset()
        for _ in range(factor):
            for item in self:
                new_dataset.append(item)
        return new_dataset

    def deepcopy(self):
        """Return a deep copy of the dataset."""
        new_dataset = BonusDataset()
        for item in self:
            new_dataset.append(copy.deepcopy(item))
        return new_dataset

    def min(self):
        """Return the minimum item in the dataset."""
        if self.length == 0:
            raise ValueError("Dataset is empty")
        min_item = self.head.data
        current = self.head.next
        while current:
            if current.data < min_item:
                min_item = current.data
            current = current.next
        return min_item

    def max(self):
        """Return the maximum item in the dataset."""
        if self.length == 0:
            raise ValueError("Dataset is empty")
        max_item = self.head.data
        current = self.head.next
        while current:
            if current.data > max_item:
                max_item = current.data
            current = current.next
        return max_item
