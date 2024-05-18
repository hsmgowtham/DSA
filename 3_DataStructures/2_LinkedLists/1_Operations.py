class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtbeg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return

    def insertAtPos(self, data, pos):
        new_node = Node(data)
        current_node = self.head
        c = 1
        while pos - 1 != c:
            current_node = current_node.next
            c += 1
        new_node.next = current_node.next
        current_node.next = new_node
        return

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next


ll = LinkedList()
ll.insertAtbeg(5)
ll.insertAtbeg(6)
ll.insertAtEnd(8)
ll.insertAtPos(9, 2)
ll.printLL()
