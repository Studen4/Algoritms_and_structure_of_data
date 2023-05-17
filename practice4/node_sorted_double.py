"""This module provides classes for representing sorted doubly linked lists."""

from node_double_linked import DoubleLinked


class SortedDouble(DoubleLinked):
    """
    Class representing a sorted doubly linked list.
    This class extends the functionality of a doubly linked list and ensures
    that the elements are always sorted in ascending order.
    """

    def is_ordered(self):
        """
        Check if the list is ordered.
        Returns:
            bool: True if the list is ordered in ascending order, False otherwise.
        """
        if not self.head or not self.head.next:
            return True

        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        """
        Sort the list in ascending order.
        This method uses the merge sort algorithm to sort the list in place.
        """
        if not self.head or not self.head.next:
            return
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        """
        Recursively perform merge sort on the list.
        Args:
            head (Node): The head node of the sublist to be sorted.
        Returns:
            Node: The head node of the sorted sublist.
        """
        if not head or not head.next:
            return head
        mid = self._get_middle_node(head)
        mid_next = mid.next
        mid.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(mid_next)
        return self._merge(left, right)

    @staticmethod
    def _get_middle_node(head):
        """
        Find the middle node of a sublist.
        Args:
            head (Node): The head node of the sublist.
        Returns:
            Node: The middle node of the sublist.
        """
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _merge(self, left, right):
        """
        Merge two sorted lists into a single sorted sublist.
        Args:
            left (Node): The head node of the left sublist.
            right (Node): The head node of the right sublist.
        Returns:
            Node: The head node of the merged sorted sublist.
        """
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)
        result.next.prev = result
        result.prev = None
        return result
