"""
In Python stack can be represented as list but it has some major downsides
Prefered thing for stack objects is deque from collections
"""


from collections import deque


# Recreation of original stack object in python:


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]


def reverse_string(string):
    stack = Stack()
    reversed_string = []

    for i in string:
        stack.push(i)

    for j in range(stack.size()):
        reversed_string.append(stack.pop())

    return ''.join(reversed_string)
