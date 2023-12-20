class queue:
    def __init__(self,size):
        self.size = size
        self.myqueue = [None]*size
        self.front = 0
        self.tail = 0
        
    def isFull(self):
        return self.tail == self.size
        
    def isEmpty(self):
        return self.front == self.tail
        
    def latest(self):
        return self.myqueue[self.fornt]
        
    def enqueue(self,item):
        if self.isFull() == False:
            self.myqueue[self.front] = item
            print("Enquque = " + str(item))
            self.tail += 1
        else:
            print("Your Queue is Full.")
    
    def dequeue(self):
        if self.isEmpty() == False:
            value = self.myqueue[self.tail - 1]
            print(str(value) + " is dequed from the queue.")
            self.tail -= 1
            return value
        else:
            print("Your Queue is Empty.")
            
    def sizenow(self):
        print("\nThe number of elemnt in queue right now are " + str(self.tail))
        return self.tail
            
my = queue(5)
my.enqueue(1)
my.enqueue(2)
my.enqueue(3)
my.enqueue(4)
my.dequeue()
my.sizenow()
