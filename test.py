from Queue_u_array import queue

myqueue = queue(5)

myqueue.quEmpty()
print("\n")
myqueue.enqueue(5)
myqueue.enqueue("Vinay")
myqueue.enqueue("Rajat")
myqueue.enqueue("Yash")
myqueue.enqueue("Lakshay")
print("\n")
myqueue.quFull()
print("\n")
myqueue.dequeue()
myqueue.dequeue()
print("\n")
myqueue.sizenow()
print("\n")
myqueue.queue