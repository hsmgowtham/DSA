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
