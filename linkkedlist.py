class node:
    def __init__(self,data,next):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def insert_first(self,e):
        newest = node(e,None)
        if self.isEmpty():
            self.head = newest
            self.tail = newest
        else:
            newest.next = self.head
            self.head = newest
        self.size += 1
            
    def insert_end(self,e):
        newest = node(e,None)
        if self.isEmpty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            self.tail = newest
        self.size += 1
        
    def insert_any(self,e,pos):
        newest = node(e,None)
        temp = self.head
        i = 1 # intital at 1st pos
        while i < pos - 1:
            temp = temp.next
            i += 1
        # after this our temp will be one node before the the pos we want to insert the new node
        newest.next = temp.next
        temp.next = newest
        self.size += 1
        
    def delete_first(self):
        if self.isEmpty():
            print("Error: Can't use delete_first() your list is Empty.")
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            if self.isEmpty():
                self.tail = None
        return value
            
    def delete_end(self):
        if self.isEmpty():
            print("Error: Cant't use delete_end() your list is Empty.")
        else:
            temp = self.head
            i = 1
            while i <= (self.size - 2):
                temp = temp.next
                i += 1
            #  using this our temp will reach at the node before tail node
            self.tail = temp # moving tail pointer backward
            temp = temp.next # moving temp pointer to last 
            value = temp.data # geting the value we are deleting
            self.tail.next = None # making next of tail pointer as None
            temp = None # making temp as None
            self.size -= 1
        return value
    
    def delete_any(self,pos):
        if self.isEmpty():
            print("Error: Can't use delete_any() your list is Empty.")
        else:
            temp = self.head
            i = 1
            while i < pos - 2:
                temp = temp.next
                i += 1
            value = temp.next.data
            temp.next = temp.next.next
            self.size -= 1
        return value
        
    def displaylist(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ] --> [ ")
            temp = temp.next
        print("x ]")

nasu = linkedlist()
nasu.isEmpty()
nasu.insert_end(10)
nasu.insert_end(20)
nasu.insert_end(30)
nasu.insert_end(40)
nasu.insert_end(50)
nasu.insert_end(60)
nasu.displaylist()
print("\n")
nasu.insert_first(5)
nasu.insert_first(1)
nasu.displaylist()
nasu.insert_any(15,3)
print("\n")
nasu.displaylist()
print("we delete the value : ",nasu.delete_first())
print("we delete the value : ",nasu.delete_end())
print("we deleted the value : ",nasu.delete_any(3))
print("\n")
nasu.displaylist()
print("size of te linked list is ",nasu.length())