"""Module implementing various data structures with limited capacity."""
import pytest
from limited_main import LimitedStack, MassiveStack, Queue, \
    PriorityQueue, MassiveQueue
from limited_linked_list import LimitedLinkedList
from limited_massive import Massive
from limited_deque import Deque


def test_limited_stack():
    """Test for linked list stack"""
    stack = LimitedStack()
    assert stack.is_empty() is True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.is_empty() is False
    assert stack.peek() == 30
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.is_empty() is False
    assert stack.peek() == 10
    stack.push(40)
    stack.push(50)
    assert stack.is_empty() is False
    assert stack.peek() == 50
    assert stack.pop() == 50
    assert stack.pop() == 40
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_massive_stack():
    """Test for massive stack"""
    stack = MassiveStack()
    assert stack.is_empty() is True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.is_empty() is False
    assert stack.peek() == 30
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.is_empty() is False
    assert stack.peek() == 10
    assert stack.pop() == 10
    assert stack.is_empty() is True


def test_limited_linked_list():
    """Test for linked list"""
    linked_list = LimitedLinkedList()
    assert linked_list.is_empty() is True
    assert linked_list.get_size() == 0
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    assert linked_list.is_empty() is False
    assert linked_list.get_size() == 3
    assert linked_list.contains(10) is True
    assert linked_list.contains(20) is True
    assert linked_list.contains(30) is True
    assert linked_list.contains(40) is False
    linked_list.remove(20)
    assert linked_list.get_size() == 2
    assert linked_list.contains(20) is False
    linked_list.remove(10)
    linked_list.remove(30)
    assert linked_list.is_empty() is True
    assert linked_list.get_size() == 0
    assert linked_list.contains(10) is False
    assert linked_list.contains(30) is False


def test_massive():
    """Test for massive"""
    massive = Massive()
    assert len(massive) == 0
    assert repr(massive) == "[]"
    massive.append(10)
    massive.append(20)
    massive.append(30)
    assert len(massive) == 3
    assert repr(massive) == "[10, 20, 30]"
    massive.insert(1, 15)
    assert len(massive) == 4
    assert repr(massive) == "[10, 15, 20, 30]"
    assert massive.index(15) == 1
    assert massive[2] == 20
    massive.remove(15)
    assert len(massive) == 3
    assert repr(massive) == "[10, 20, 30]"
    try:
        massive.index(15)
        assert False
    except ValueError:
        assert True
    massive[0] = 5
    assert massive[0] == 5
    massive[2] = 30
    assert massive[2] == 30
    massive.remove(30)
    assert len(massive) == 2
    assert repr(massive) == "[5, 20]"


def test_queue():
    """Test queue for linked list"""
    queue = Queue()
    assert queue.is_empty() is True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.is_empty() is False
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty() is True
    assert queue.dequeue() is None


def test_priority_queue():
    """Test for linked list priority queue"""
    priority_queue = PriorityQueue()
    assert priority_queue.is_empty() is True
    priority_queue.enqueue_with_priority("low", 5)
    priority_queue.enqueue_with_priority("medium", 10)
    priority_queue.enqueue_with_priority("high", 15)
    assert priority_queue.is_empty() is False
    assert priority_queue.peek() == ("high", 15)
    assert priority_queue.dequeue_highest_priority() == "high"
    assert priority_queue.dequeue_highest_priority() == "medium"
    assert priority_queue.dequeue_highest_priority() == "low"
    assert priority_queue.is_empty() is True
    assert priority_queue.dequeue_highest_priority() is None


def test_massive_queue():
    """Test queue for massive"""
    massive_queue = MassiveQueue()
    assert massive_queue.is_empty() is True
    massive_queue.enqueue(1)
    massive_queue.enqueue(2)
    massive_queue.enqueue(3)
    assert massive_queue.is_empty() is False
    assert massive_queue.dequeue() == 1
    assert massive_queue.dequeue() == 2
    assert massive_queue.dequeue() == 3
    assert massive_queue.is_empty() is True
    with pytest.raises(ValueError):
        massive_queue.dequeue()


def test_deque():
    """Test deque for linked list"""
    deque = Deque()
    assert deque.is_empty() is True
    deque.add_front(1)
    deque.add_front(2)
    deque.add_rear(3)
    assert deque.is_empty() is False
    assert deque.peek_front() == 2
    assert deque.peek_rear() == 3
    assert deque.remove_front() == 2
    assert deque.remove_rear() == 3
    assert deque.remove_front() == 1
    assert deque.is_empty() is True
    assert deque.peek_front() is None
    assert deque.peek_rear() is None
    assert deque.remove_front() is None
    assert deque.remove_rear() is None


def test_deque_with_multiple_elements():
    """Test deque for linked list part 2"""
    deque = Deque()
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(3)
    deque.add_rear(4)
    assert deque.is_empty() is False
    assert deque.peek_front() == 3
    assert deque.peek_rear() == 4
    assert deque.remove_front() == 3
    assert deque.remove_rear() == 4
    assert deque.remove_front() == 1
    assert deque.remove_rear() == 2
    assert deque.is_empty() is True
    assert deque.peek_front() is None
    assert deque.peek_rear() is None
    assert deque.remove_front() is None
    assert deque.remove_rear() is None


def test_empty_deque():
    """Test deque for linked list part 3"""
    deque = Deque()
    assert deque.is_empty() is True
    assert deque.peek_front() is None
    assert deque.peek_rear() is None
    assert deque.remove_front() is None
    assert deque.remove_rear() is None
    deque.add_front(1)
    assert deque.is_empty() is False
    assert deque.peek_front() == 1
    assert deque.peek_rear() == 1
    assert deque.remove_front() == 1
    assert deque.is_empty() is True
    assert deque.peek_front() is None
    assert deque.peek_rear() is None
    assert deque.remove_front() is None
    assert deque.remove_rear() is None


def test_remove_rear_with_multiple_elements():
    """Test deque for linked list test 4"""
    deque = Deque()
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(3)
    deque.add_rear(4)
    assert deque.remove_rear() == 4
    assert deque.remove_rear() == 2
    assert deque.remove_rear() == 1
    assert deque.remove_rear() == 3
    assert deque.is_empty() is True
    assert deque.peek_front() is None
    assert deque.peek_rear() is None
    assert deque.remove_rear() is None


def all_tests():
    """All tests starter"""
    test_limited_stack()
    test_massive_stack()
    test_limited_linked_list()
    test_massive()
    test_queue()
    test_priority_queue()
    test_massive_queue()
    test_deque()
    test_empty_deque()
    test_deque_with_multiple_elements()
    test_remove_rear_with_multiple_elements()


if __name__ == "__main__":
    all_tests()
