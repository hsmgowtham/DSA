class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"{str(self.data)}"


class Stack:
    def __init__(self) -> None:
        self.top = -1
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return

    def pop(self):
        if self.head:
            if self.head.next:
                self.head = self.head.next
                return
        raise Exception("Error: No Nodes Left to pop")

    def peek(self):
        print(self.head.data)

    def printStack(self):
        current_node = self.head
        while current_node:
            print(current_node, end=" -> ")
            current_node = current_node.next
        print()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.printStack()
s.pop()
s.printStack()
s.peek()
s.pop()
s.printStack()
s.pop()
s.printStack()
s.pop()
s.printStack()
