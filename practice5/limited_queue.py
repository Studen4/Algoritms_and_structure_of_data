"""Module implementing a queue and a queue with priority
 using a limited linked list."""

from limited_linked_list import LimitedLinkedList


class Queue:
    """Class representing a Queue."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """
        Check if the queue is empty.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.size == 0

    def enqueue(self, element):
        """
        Enqueue an element to the end of the queue.
        Args:
            element: The element to be enqueued.
        """
        new_node = LimitedLinkedList.Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        """
        Dequeue the element from the front of the queue.
        Returns:
            The dequeued element, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        element = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return element

    def peek(self):
        """
        Get the element at the front of the queue without deque it.
        Returns:
            The element at the front of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.head.data


class PriorityQueue(Queue):
    """
    Class representing a PriorityQueue, which is a subclass of Queue.
    """
    def enqueue_with_priority(self, element, priority):
        """
        Enqueue an element with a given priority.
        Args:
            element: The element to be enqueued.
            priority: The priority of the element.
        """
        new_node = LimitedLinkedList.Node((element, priority))
        if self.is_empty() or priority > self.head.data[1]:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and priority <= current.next.data[1]:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def dequeue_highest_priority(self):
        """
        Dequeue the element with the highest priority.
        Returns:
            The dequeued element with the highest priority, or None if the priority queue is empty.
        """
        if self.is_empty():
            return None
        element = self.head.data[0]
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return element


class MassiveQueue:
    """
    Class representing a queue implemented using a list (massive).
    """

    def __init__(self):
        self.queue = []

    def is_empty(self):
        """
        Checks if the queue is empty.
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def enqueue(self, element):
        """
        Enqueues an element to the end of the queue.
        Args:
            element: The element to be enqueued.
        """
        self.queue.append(element)

    def dequeue(self):
        """
        Dequeues the element from the front of the queue.
        Returns:
            The dequeued element.
        Raises:
            ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.queue.pop(0)
