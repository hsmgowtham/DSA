class Node:
    def __init__(self, data, prev_node=None):
        self.pre = prev_node
        self.data = data
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, data):
        new_node = Node(data=data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.pre = new_node
        self.head = new_node
        return

    def insertAtEnd(self, data):
        new_node = Node(data=data)
        current_node = self.head
        if not self.head:
            self.head = new_node
            return
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.pre = current_node
        return

    def insertAtPos(self, data, pos):
        new_node = Node(data)
        current_node = self.head
        c = 1
        prev_node = None
        while pos != c:
            prev_node = current_node
            current_node = current_node.next
            c += 1
        prev_node.next = new_node
        new_node.pre = prev_node
        new_node.next = current_node
        current_node.pre = new_node
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


ll = DoublyLL()
print("--- Insert At Beg 5 ---")
ll.insertAtBeg(5)
ll.printLL()
print("--- Insert At Beg 6 ---")
ll.insertAtBeg(6)
ll.printLL()
print("--- Insert At End 8,10,11,12 ---")
ll.insertAtEnd(8)
ll.insertAtEnd(10)
ll.insertAtEnd(11)
ll.insertAtEnd(12)
ll.printLL()
print("--- Insert At Pos 2 = 9 ---")
ll.insertAtPos(9, 2)
ll.printLL()
print("--- Search 6 ---")
ll.search(6)
print("--- Search 8 ---")
ll.search(8)
