"""
Infix to Postfix:

Example 1:
Input: x+y*z/w+u
Output: ++x/*yzwu
Explanation: Infix to prefix

Example 2:
Input: a+b
Output: +ab
Explanation: Infix to prefix

Algorithm:
reverse the string
if exp[i] == (
    push to stack
elif exp[i] == operand
    add to result
elif exp[i] == )
    pop and add to result until ( is encountered in the stack
else 
    if exp[i] is a operator
    while (not s.is_empty()) and (
            (getOperatorPrecedence[exp[i]] < getOperatorPrecedence.get(s.peek(), -1))
            or (
                (
                    getOperatorPrecedence[exp[i]]
                    <= getOperatorPrecedence.get(s.peek(), -1)
                )
                and exp[i] == "^"
            )
        )
        add peek element to result
    push exp[i] to stack
reverse the string
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
exp = "x+y*z/w+u"
res = ""

for i in range(len(exp) - 1, -1, -1):
    if exp[i] == "(":
        s.push(exp[i])
    elif exp[i].isalnum():
        res += exp[i]
    elif exp[i] == ")":
        while s.peek() != "(" and not s.is_empty():
            res += s.pop()
        s.pop()
    else:
        # # if it's a operator
        while (not s.is_empty()) and (
            (getOperatorPrecedence[exp[i]] < getOperatorPrecedence.get(s.peek(), -1))
            or (
                (
                    getOperatorPrecedence[exp[i]]
                    <= getOperatorPrecedence.get(s.peek(), -1)
                )
                and exp[i] == "^"
            )
        ):
            res += s.pop()
        s.push(exp[i])
while not s.is_empty():
    res += s.pop()

# reverse the output
print("Prefix Exp:")
for i in range(len(res) - 1, -1, -1):
    print(res[i], end="")
print()
