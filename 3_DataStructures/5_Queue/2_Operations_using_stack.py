from queue import LifoQueue


class MyQueue:
    def __init__(self) -> None:
        self.input_stack = LifoQueue()
        self.output_stack = LifoQueue()

    def push(self, x):
        self.input_stack.put(x)

    def pop(self):
        if self.output_stack.empty():
            while not self.input_stack.empty():
                self.output_stack.put(self.input_stack.get())
        # remove top element in the output stack which is 1st element in the queue
        ele = self.output_stack.get()
        return ele

    def top(self) -> int:
        # shift input to output
        if self.output_stack.empty():
            while not self.input_stack.empty():
                self.output_stack.put(self.input.get())
        return self.output_stack.queue[-1]

    def size(self) -> int:
        return self.input_stack.qsize() + self.output_stack.qsize()


q = MyQueue()
q.push(3)
q.push(4)
print("The element poped is ", q.pop())
q.push(5)
print("The top of the queue is ", q.top())
print("The size of the queue is ", q.size())
