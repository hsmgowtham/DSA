"""
Infix to Postfix:

Example 1:
Input: a+b*(c^d-e)^(f+g*h)-i
Output: abcd^e-fgh*+^*+i-
        abcd^e-fgh*+^*+i
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
        self.stack.append(ele)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(list(self.stack))


getOperatorPrecedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

s = Stack()
exp = "a+b*(c^d-e)^(f+g*h)-i"
res = ""

for char in exp:
    if char == "(":
        s.push(char)
    elif char.isalnum():
        res += char
    elif char == ")":
        while s.peek() != "(" and not s.is_empty():
            res += s.pop()
        s.pop()
    else:
        # # if it's a operator
        while (not s.is_empty()) and (
            getOperatorPrecedence[char] <= getOperatorPrecedence.get(s.peek(), -1)
        ):
            res += s.pop()
        s.push(char)
while not s.is_empty():
    res += s.pop()
print("Postfix Exp:", res)
