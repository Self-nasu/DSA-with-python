class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linklist:
    def __init__(self):
        self.head = None # head pointer in linklist
        self.tail = None # tail pointer in linklist
        
    # Some cheking functions
    def listEmpty(self):
        output = False
        if self.head == self.tail:
            output = True
            print("Your Linklist is Empty.")
        return output
    
    # Now function to inster in list
    
    # insert at the end
    def insert_at_tail(self,data):
        new_node = node(data)
        if not self.head
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail
            temp = new_node
            self.tail = new_node    
    
    # insert at the start
    def insert_at_head(self,data):
        new_node = node(data) 
        new_node.next = self.head # seting new node next pointer to head
        self.head = new_node # changing the head to new node
        self.tail = new_node #
        
    # deletaion of node in linkedlist
    
    def delete_node(self,data):
        temp = self.head
        if temp.data == data:
            self.head = temp.next
            temp = None
            return
        while temp.next != data:
            temp = temp.next
        temp2 = temp.next
        temp.next = temp2.next
        temp2 = None
        temp = None
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="]--->[")
            temp = temp.next
        print("X")

Mylist = linklist()

Mylist.insert_at_tail(1)        
Mylist.insert_at_tail(2)        
Mylist.insert_at_tail(3)        
Mylist.insert_at_tail(4)

Mylist.display()        
        