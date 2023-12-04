class queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.size = size # total size of the queue
        self.front = 0 # initaly first node of the queue is at 0
        self.tail = 0 # initaly last node of the queue is also at 0

    def quFull(self):
        # when the tail and size varibale will be equal we say the queue if full
        output = False
        if self.tail == self.size:
            output = True
            print("Your Queue is Full.")
        return output
    
    def quEmpty(self):
        # when the front and tail variable will be equal we say that the queue if empty
        output = False
        if self.front == self.tail:
            output = True
            print("Your Queue is Empty.")
        return output
    
    # Now in queue we only have to enqueue and dequeue the item from one end only as it follow : FIFO
    
    def enqueue(self,item):
        if self.quFull() == False:
            self.queue[self.tail] = item
            print(str(item) + " is enqueue at index " + str(self.tail))
            self.tail += 1
        else:
            print("Error: Your Queue is Full")
            
    def dequeue(self):
        if self.quEmpty() == False:
            dequeue_item = self.queue[self.tail - 1]
            print(str(dequeue_item) + " item is dequeue from queue from index " + str(self.tail -1))
            self.tail -= 1
            return dequeue_item
        else:
            print("Error: Your Queue is Empty")
    
    def sizenow(self):
        sizenow = self.tail + 1
        return sizenow
    
    def latest(self):
        if self.quEmpty == False:
            print("the latest item enqueued in Queue is " + str(self.queue[self.front]))
        else:
            print("Your Queue is Empty")