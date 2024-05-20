class Node:
    def __init__(self, data, prev_node=None):
        self.pre = prev_node
        self.data = data
        self.next = None
    
    def __str__(self):
        prev_data = self.pre.data if self.pre else "None"
        next_data = self.next.data if self.next else "None"
        return f"|{prev_data}|N({self.data})|{next_data}|"


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
            print(current_node, end=" -> ")
            current_node = current_node.next
        print()
    
    def removeNode(self, data):
        prev_node = None
        next_node = None
        current_node = self.head
        if self.head.data == data:
            self.head = self.head.next
            self.head.pre = None
            return
        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
            if current_node.next:
                next_node = current_node.next
            else:
                next_node = None
        prev_node.next = next_node
        if next_node:
            next_node.pre = prev_node
        return


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
ll.printLL()
print("--- Remove Node with data 9 ---")
ll.removeNode(9)
ll.printLL()
print("--- Remove Node with data 12 ---")
ll.removeNode(12)
ll.printLL()