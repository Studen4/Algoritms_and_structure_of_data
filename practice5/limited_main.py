"""Module with visual part of all limited data structures"""
from limited_stack import LimitedStack, MassiveStack
from limited_queue import Queue, PriorityQueue, MassiveQueue
from limited_deque import Deque


def stack_work_show():
    """Demonstrate work of stack"""
    stack = LimitedStack()
    print("Linked List test - 1")
    print("Is stack empty?", stack.is_empty())  # Expected output: True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Is stack empty?", stack.is_empty())  # Expected output: False
    print("Top element of the stack:", stack.peek())  # Expected output: 30
    print("Popped element from the stack:", stack.pop())  # Expected output: 30
    print("Popped element from the stack:", stack.pop())  # Expected output: 20
    print("Is stack empty?", stack.is_empty())  # Expected output: False
    print("Top element of the stack:", stack.peek())  # Expected output: 10
    stack.push(40)
    stack.push(50)
    print("Is stack empty?", stack.is_empty())  # Expected output: False
    print("Top element of the stack:", stack.peek())  # Expected output: 50
    print("Popped element from the stack:", stack.pop())  # Expected output: 50
    print("Popped element from the stack:", stack.pop())  # Expected output: 40
    print("Popped element from the stack:", stack.pop())  # Expected output: 10
    print("Is stack empty?", stack.is_empty())  # Expected output: True
    print("Massive test - 2")
    stack = MassiveStack()
    print("Is stack empty?", stack.is_empty())  # Expected output: True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Is stack empty?", stack.is_empty())  # Expected output: False
    print("Top element of the stack:", stack.peek())  # Expected output: 30
    print("Popped element from the stack:", stack.pop())  # Expected output: 30
    print("Popped element from the stack:", stack.pop())  # Expected output: 20
    print("Is stack empty?", stack.is_empty())  # Expected output: False
    print("Top element of the stack:", stack.peek())  # Expected output: 10
    print("Popped element from the stack:", stack.pop())  # Expected output: 10
    print("Is stack empty?", stack.is_empty())  # Expected output: True


def queue_work_show():
    """Demonstrate work of queue"""
    queue = Queue()
    print("Linked List test - 1")
    print("Is queue empty?", queue.is_empty())  # Expected output: True
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Is queue empty?", queue.is_empty())  # Expected output: False
    print("Front element of the queue:", queue.peek())  # Expected output: 10
    print("Dequeued element:", queue.dequeue())  # Expected output: 10
    print("Dequeued element:", queue.dequeue())  # Expected output: 20
    print("Is queue empty?", queue.is_empty())  # Expected output: False
    print("Front element of the queue:", queue.peek())  # Expected output: 30
    queue.enqueue(40)
    queue.enqueue(50)
    print("Is queue empty?", queue.is_empty())  # Expected output: False
    print("Front element of the queue:", queue.peek())  # Expected output: 30
    print("Dequeued element:", queue.dequeue())  # Expected output: 30
    print("Dequeued element:", queue.dequeue())  # Expected output: 40
    print("Dequeued element:", queue.dequeue())  # Expected output: 50
    print("Is queue empty?", queue.is_empty())  # Expected output: True
    print("Massive test - 2")
    queue = MassiveQueue()
    print("Is queue empty?", queue.is_empty())  # Expected output: True
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Is queue empty?", queue.is_empty())  # Expected output: False
    print("Dequeued element:", queue.dequeue())  # Expected output: 10
    print("Dequeued element:", queue.dequeue())  # Expected output: 20
    print("Is queue empty?", queue.is_empty())  # Expected output: False
    print("Dequeued element:", queue.dequeue())  # Expected output: 30
    print("Is queue empty?", queue.is_empty())  # Expected output: True


def priority_queue_work_show():
    """Demonstrate work of priority queue"""
    priority_queue = PriorityQueue()
    print("Is priority queue empty?", priority_queue.is_empty())  # Expected output: True
    priority_queue.enqueue_with_priority("Task 1", 3)
    priority_queue.enqueue_with_priority("Task 2", 1)
    priority_queue.enqueue_with_priority("Task 3", 2)
    print("Is priority queue empty?", priority_queue.is_empty())  # Expected output: False
    print("Highest priority task:", priority_queue.peek())  # Expected output: Task 1
    print("Dequeued highest priority task:",
          priority_queue.dequeue_highest_priority())  # Expected output: Task 1
    print("Dequeued highest priority task:",
          priority_queue.dequeue_highest_priority())  # Expected output: Task 3
    print("Is priority queue empty?", priority_queue.is_empty())  # Expected output: False
    print("Highest priority task:", priority_queue.peek())  # Expected output: Task 2
    priority_queue.enqueue_with_priority("Task 4", 2)
    priority_queue.enqueue_with_priority("Task 5", 1)
    print("Is priority queue empty?", priority_queue.is_empty())  # Expected output: False
    print("Highest priority task:", priority_queue.peek())  # Expected output: Task 4
    print("Dequeued highest priority task:",
          priority_queue.dequeue_highest_priority())  # Expected output: Task 4
    print("Dequeued highest priority task:",
          priority_queue.dequeue_highest_priority())  # Expected output: Task 2
    print("Dequeued highest priority task:",
          priority_queue.dequeue_highest_priority())  # Expected output: Task 5
    print("Is priority queue empty?", priority_queue.is_empty())  # Expected output: True


def deque_work_show():
    """Demonstrate work of deque"""
    deque = Deque()
    print("Is deque empty?", deque.is_empty())  # Expected output: True
    deque.add_front("A")
    deque.add_front("B")
    deque.add_rear("C")
    print("Is deque empty?", deque.is_empty())  # Expected output: False
    print("Front of deque:", deque.peek_front())  # Expected output: B
    print("Rear of deque:", deque.peek_rear())  # Expected output: C
    print("Removed front element:", deque.remove_front())  # Expected output: B
    print("Removed rear element:", deque.remove_rear())  # Expected output: C
    print("Is deque empty?", deque.is_empty())  # Expected output: False
    print("Front of deque:", deque.peek_front())  # Expected output: A
    print("Rear of deque:", deque.peek_rear())  # Expected output: A
    deque.add_front("D")
    deque.add_rear("E")
    print("Is deque empty?", deque.is_empty())  # Expected output: False
    print("Front of deque:", deque.peek_front())  # Expected output: D
    print("Rear of deque:", deque.peek_rear())  # Expected output: E
    print("Removed front element:", deque.remove_front())  # Expected output: D
    print("Removed rear element:", deque.remove_rear())  # Expected output: E
    print("Is deque empty?", deque.is_empty())  # Expected output: True


if __name__ == "__main__":
    stack_work_show()
    queue_work_show()
    priority_queue_work_show()
    deque_work_show()
