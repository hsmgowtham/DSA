"""
Prefix to Postfix
Input :  Prefix :  *+AB-CD
Output : Postfix : AB+CD-*

Input :  Prefix :  *-A/BC-/AKL
Output : Postfix : ABC/-AK/L-*

- Read the Prefix expression in reverse order (from right to left)
- If the symbol is an operand, then push it onto the Stack
- If the symbol is an operator, then pop two operands from the Stack 
    - Create a string by concatenating the two operands and the operator after them. 
    - string = operand1 + operand2 + operator 
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


def prefixToPostfix(string):
    st = Stack()
    for i in range(len(string) - 1, -1, -1):
        if string[i].isalnum():
            st.push(string[i])
        else:
            res = st.pop() + st.pop() + string[i]
            st.push(res)
    return st.pop()


print(prefixToPostfix("*+AB-CD"))
print(prefixToPostfix("*-A/BC-/AKL"))
