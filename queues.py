from collections import deque


q = deque()


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        return self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
