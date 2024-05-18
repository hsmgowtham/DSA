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

    def search(self, data):
        pos = 1
        current_node = self.head
        while current_node.data != data:
            current_node = current_node.next
            pos += 1
        else:
            if current_node.data == data:
                print(f"Found at Index {pos}")
            else:
                print("Given Data Not Found")

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print()


ll = LinkedList()
ll.insertAtbeg(5)
ll.insertAtbeg(6)
ll.insertAtEnd(8)
ll.insertAtPos(9, 2)
ll.search(6)
ll.search(8)
ll.printLL()
