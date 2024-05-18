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
        if self.head is None:
            self.head = new_node
            return
        else:
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

    def remove_node(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        prev_node = None

        while current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = current_node.next
        return

    def remove_first_node(self):
        if self.head:
            self.head = self.head.next
            return

    def remove_end_node(self):
        current_node = self.head
        prev_node = None
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
        return
    
    def remove_node_at_pos(self, pos):
        current_node = self.head
        prev_node = None
        c = 1
        if pos == 1:
            self.head = self.head.next
            return 
        
        while pos != c:
            prev_node = current_node
            current_node = current_node.next
            c += 1
        prev_node.next = current_node.next
        return


ll = LinkedList()
ll.insertAtbeg(5)
ll.insertAtbeg(6)
ll.insertAtEnd(8)
ll.insertAtEnd(10)
ll.insertAtEnd(11)
ll.insertAtEnd(12)
ll.insertAtPos(9, 2)
ll.search(6)
ll.search(8)
ll.printLL()
ll.remove_node(5)
ll.printLL()
ll.remove_first_node()
ll.printLL()
ll.remove_end_node()
ll.printLL()
ll.remove_node_at_pos(3)
ll.printLL()
