"""
Postfix to Infix
Input : abc++
Output : (a + (b + c))

Input  : ab*c+
Output : ((a*b)+c)

- Read the Prefix expression in reverse order (from left to right)
- If the symbol is an operand, then push it onto the Stack
- If the symbol is an operator, then pop two operands from the Stack 
    - Create a string by concatenating the two operands and the operator after them. 
    - string = operand2 + operator + operand1
    - And push the resultant string back to Stack
- Repeat the above steps until end of Prefix expression.
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


def postfixToPrefix(string):
    st = Stack()
    for i in range(0, len(string)):
        if string[i].isalnum():
            st.push(string[i])
        else:
            op1 = st.pop()
            op2 = st.pop()
            res =  "(" + op2 + string[i] + op1 + ")"
            st.push(res)
    return st.pop()


print(postfixToPrefix("abc++"))
print(postfixToPrefix("ab*c+"))
