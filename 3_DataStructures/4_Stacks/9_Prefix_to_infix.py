"""
Prefix to Infix
Input :  Prefix :  *+AB-CD
Output : Infix : ((A+B)*(C-D))

Input :  Prefix :  *-A/BC-/AKL
Output : Infix : ((A-(B/C))*((A/K)-L))

- Read the Prefix expression in reverse order (from right to left)
- If the symbol is an operand, then push it onto the Stack
- If the symbol is an operator, then pop two operands from the Stack 
    - Create a string by concatenating the two operands and the operator between them. 
    - string = (operand1 + operator + operand2) 
    - And push the resultant string back to Stack
- Repeat the above steps until the end of Prefix expression.
- At the end stack will have only 1 string i.e resultant string
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


def prefixToInfix(string):
    st = Stack()
    for i in range(len(string) - 1, -1, -1):
        if string[i].isalnum():
            st.push(string[i])
        else:
            res = "(" + st.pop() + string[i] + st.pop() + ")"
            st.push(res)
    return st.pop()


print(prefixToInfix("*+AB-CD"))
print(prefixToInfix("*-A/BC-/AKL"))
