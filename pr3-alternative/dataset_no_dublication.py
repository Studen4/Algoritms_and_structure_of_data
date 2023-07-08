"""Module with no duplication realisation of dataset."""
from level_3_dataset import BonusDataset


class NoDuplicationDataset(BonusDataset):
    """Class with realisation of no-dub function."""

    def unique(self):
        """Return a new dataset with duplicate elements removed."""
        unique_dataset = BonusDataset()
        visited = set()
        current = self.head
        while current:
            if current.data not in visited:
                unique_dataset.append(current.data)
                visited.add(current.data)
            current = current.next
        return unique_dataset
