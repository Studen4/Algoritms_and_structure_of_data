"""Module with sort realisation of dataset."""
from level_3_dataset import BonusDataset


class SortedDataset(BonusDataset):
    """Class with realisation of merge sorting to dataset."""

    def sort(self):
        """Sort the dataset in ascending order."""
        if self.length > 1:
            self.head = self._merge_sort(self.head)

    @staticmethod
    def _get_middle(head):
        """Get the middle node of the linked list."""
        if head is None:
            return head

        slow = head
        fast = head.next

        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next

        return slow

    def _merge_sort(self, head):
        """Sort the linked list using merge sort."""
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        sorted_list = self._merge(left, right)
        return sorted_list

    def _merge(self, left, right):
        """Merge two linked lists."""
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result
