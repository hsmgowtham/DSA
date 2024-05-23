from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def __str__(self):
        return str(list(self.items))

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:", queue)
    print("Dequeued item:", queue.dequeue())
    print("Queue after dequeue:", queue)
    print("Front item:", queue.peek())
    print("Queue size:", queue.size())
