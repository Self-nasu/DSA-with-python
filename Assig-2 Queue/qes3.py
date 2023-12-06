from qes2_Q_U_linklist import Queue

queue = Queue()


def display_queue(queue):
    print("Front:", queue.peek())
    queue.display()
    print()


# a. enqueue(1)
queue.enqueue(1)
display_queue(queue)

# b. enqueue(7)
queue.enqueue(7)
display_queue(queue)

# c. dequeue()
queue.dequeue()
display_queue(queue)

# d. enqueue(16)
queue.enqueue(16)
display_queue(queue)

# e. enqueue(5)
queue.enqueue(5)
display_queue(queue)

# f. dequeue()
queue.dequeue()
display_queue(queue)

# g. front()
print("Front:", queue.peek())
