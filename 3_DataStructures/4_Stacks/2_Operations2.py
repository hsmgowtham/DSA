"""
Python provides a built-in library called collections which includes a deque (double-ended queue)
 class that can be used to implement a stack efficiently. Here’s how you can implement a stack using collections.deque
"""
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(list(self.items))

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack)
    print("Popped item:", stack.pop())
    print("Stack after pop:", stack)
    print("Top item:", stack.peek())
    print("Stack size:", stack.size())
