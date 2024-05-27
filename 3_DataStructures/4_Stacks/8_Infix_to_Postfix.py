"""
Infix to Postfix:

Example 1:
Input: a+b*(c^d-e)^(f+g*h)-i
Output: abcd^e-fgh*+^*+i-
Explanation: Infix to postfix

Example 2:
Input: (p+q)*(m-n)
Output: pq+mn-*
Explanation: Infix to postfix

Algorithm:
if char == (
    push to stack
elif char == operand
    add to result
elif char == )
    pop and add to result until ( is encountered in the stack
else 
    if char is a operator
    if precedence of the operator is <= peek element in the stack
        add peek element to result
    push char to stack
"""

from collections import deque


class Stack:
    def __init__(self) -> None:
        self.stack = deque()

    def push(self, ele):
        if not self.is_empty():
            self.stack.append(ele)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()

    def is_empty(self):
        return self.stack.empty()


getOperatorPrecedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

s = Stack()
