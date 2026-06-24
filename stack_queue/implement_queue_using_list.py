"""
Problem: Implement a Queue Using a List
=========================================
Implement a FIFO queue supporting enqueue, dequeue, peek, is_empty, and size.

Interview Explanation:
    A Queue is First-In-First-Out (FIFO). Python's list can act as a queue
    but dequeue from front (pop(0)) is O(n). Better: use collections.deque
    with O(1) popleft(). For interviews, know both implementations.
    Key vocab: enqueue = add to back, dequeue = remove from front.

Time Complexity:
    enqueue:  O(1)
    dequeue:  O(n) with list (O(1) with deque)
    peek:     O(1)
"""

from collections import deque


class QueueUsingList:
    """
    Queue implemented with a Python list.
    Simple but dequeue is O(n) due to pop(0).
    """

    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Add item to the back of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return item from the front. O(n) with list."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.pop(0)

    def peek(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek on empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"


class QueueUsingDeque:
    """
    Queue implemented with collections.deque.
    O(1) enqueue and dequeue — preferred in production.
    """

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()  # O(1) with deque

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek on empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"


if __name__ == "__main__":
    print("=" * 50)
    print("Queue Implementation")
    print("=" * 50)

    q = QueueUsingDeque()
    print(f"Empty? {q.is_empty()}")

    for item in ["test_1", "test_2", "test_3"]:
        q.enqueue(item)
        print(f"Enqueued '{item}' → {q}")

    print(f"Peek: {q.peek()}")
    print(f"Dequeue: {q.dequeue()} → {q}")
    print(f"Size: {q.size()}")
