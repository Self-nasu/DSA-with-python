class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def is_empty(self):
        return len(self.stack_enqueue) == 0 and len(self.stack_dequeue) == 0

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        if not self.stack_dequeue:
            # Move all items from stack_enqueue to stack_dequeue
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        return self.stack_dequeue.pop()


queue = QueueUsingStack()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
