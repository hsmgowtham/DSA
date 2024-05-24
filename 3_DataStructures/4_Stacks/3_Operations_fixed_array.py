class Stack:
    def __init__(self) -> None:
        self.top = -1
        self.size = 7
        self.arr = [0] * self.size

    def push(self, ele):
        if self.top == self.size-1:
            raise Exception ("Error: Stack is Full, can't push element")
        self.top += 1
        self.arr[self.top]= ele
    
    def pop(self):
        if self.top == -1:
            raise Exception("Error: Stack is Empty, can't pop")
        self.top -= 1
        self.arr.pop()
    
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return (self.top + 1)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Error: Stack is Empty, not element to peek")
        return self.arr[self.top]


    def __str__(self) -> str:
        return str(self.arr)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.pop()
print(s)
print(s.peek())