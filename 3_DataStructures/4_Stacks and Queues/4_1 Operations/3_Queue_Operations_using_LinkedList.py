class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"{str(self.data)}"


class Queue:
    def __init__(self) -> None:
        self.top = -1
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return

    def pop(self):
        if self.head:
            pop_node = self.head
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return pop_node.data

        raise Exception("Error: No Nodes Left to pop")

    def peek(self):
        print("Peek Node: ", self.head.data)

    def printStack(self):
        print("Queue: ", end=" ")
        current_node = self.head
        while current_node:
            print(current_node, end=" -> ")
            current_node = current_node.next
        print()


s = Queue()
s.push(1)
s.push(2)
s.push(3)
s.printStack()
print("Popped Node: ", s.pop())
s.printStack()
s.peek()
print("Popped Node: ", s.pop())
s.printStack()
print("Popped Node: ", s.pop())
s.printStack()
print("Popped Node: ", s.pop())
s.printStack()
