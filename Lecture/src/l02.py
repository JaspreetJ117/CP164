"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2025-01-12"
-------------------------------------------------------
"""
"""
An ADT (Abstract Data Type) is a conceptual framework 
that defines how data is organized and the operations 
that can be performed on it, without specifying how it 
is implemented. It focuses on what the data structure 
does rather than how it does it.

ADT implementations:
    - List (Dynamic Array):
        Operations: Insert, delete, iterate, search, etc.
        Python implementation: List
    - Stack:
        Operations: Push, pop, peek (LIFO - Last In, First Out)
        Python implementation: list or collections.deque
    - Queue:
        Operations: Enqueue, dequeue (FIFO - First In, First Out)
        Python implementation: collections.deque or queue.Queue
    - Deque (Double-Ended Queue):
        Operations: Add/remove from both ends
        Python implementation: collections.deque
    - Set:
        Operations: Add, remove, union, intersection, etc.
        Python implementation: set
    - Dictionary (Map):
        Operations: Insert, delete, lookup by key
        Python implementation: dict
"""

# Stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
#Queue
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

# Deque
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def add_front(self, item):
        self.items.appendleft(item)

    def add_back(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Remove from empty deque")

    def remove_back(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Remove from empty deque")

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty deque")

    def peek_back(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty deque")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def size(self):
        return len(self.items)
    
"""
Summary of Operations:
Stack (LIFO):
push: Add to the top.
pop: Remove from the top.
peek: Look at the top.

Queue (FIFO):
enqueue: Add to the back.
dequeue: Remove from the front.
peek: Look at the front.

Deque (Double-Ended Queue):
add_front: Add to the front.
add_back: Add to the back.
remove_front: Remove from the front.
remove_back: Remove from the back.
"""

"""
Deepcopy what is it? Why use deepcopy? Where do I use it?
"""