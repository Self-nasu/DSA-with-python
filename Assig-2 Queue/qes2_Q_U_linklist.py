class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        else:
            return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", end=" ")
            current = self.front
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()

    print("Peek:", queue.peek())

    queue.dequeue()
    queue.display()

    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
