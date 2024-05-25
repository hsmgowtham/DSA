"""
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

"""

"""
Approach 1:
using Pairs
lets say we need to push values in below order
-2, 3, -4, 1
the pairs will be [val, min_ele_until_now]
stack will be
[1,-4]
[-4,-2]
[3,-2]
[-2,-2]
get min returns -4
pop()
get min returns -2
"""


class Pair:
    def __init__(self, ele, min_val_till_now) -> None:
        self.ele = ele
        self.min_val_till_now = min_val_till_now


class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.top = -1

    def push(self, ele):
        if self.top == -1:
            self.stack.append(Pair(ele, ele))
            self.top += 1
            return ele
        min_ele = min(ele, self.stack[self.top].min_val_till_now)
        self.top += 1
        self.stack.append(Pair(ele, min_ele))
        return ele

    def empty(self):
        return self.top == -1

    def pop(self):
        if self.empty():
            raise Exception("Error: Stack is Empty")
        self.top -= 1
        return self.stack.pop().ele

    def peek(self):
        return self.stack[self.top].ele

    def getMin(self):
        if not self.empty():
            return self.stack[self.top].min_val_till_now


s = Stack()
print("Pushed:  ", s.push(-2))
print("Peek ele: ", s.peek())
print("Pushed:  ", s.push(3))
print("Peek ele: ", s.peek())
print("Pushed:  ", s.push(-4))
print("Peek ele: ", s.peek())
print("Pushed:  ", s.push(1))
print("Peek ele: ", s.peek())
print("Min ele", s.getMin())
print("Pop: ", s.pop())
print("Min ele", s.getMin())
print("Pop: ", s.pop())
print("Min ele", s.getMin())

