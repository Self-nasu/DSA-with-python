from queue import Queue


class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def is_empty(self):
        return self.queue1.empty()

    def push(self, item):
        # Push the item to queue1
        self.queue1.put(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None

        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        popped_item = self.queue1.get()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_item

    def top(self):
        if self.is_empty():
            print("Stack is empty.")
            return None

        top_item = None
        while not self.queue1.empty():
            top_item = self.queue1.get()
            self.queue2.put(top_item)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_item


stack = StackUsingQueue()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top:", stack.top())
print("Popped:", stack.pop())

print("Top:", stack.top())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
