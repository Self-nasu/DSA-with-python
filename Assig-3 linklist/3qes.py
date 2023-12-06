class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_nth_node_from_end(self, n):
        if not self.head or n <= 0:
            return None

        first = self.head
        second = self.head

        for i in range(n):
            if first is None:
                return None
            first = first.next

        while first:
            first = first.next
            second = second.next

        return second.data if second else None

# example
llist = LinkedList()
llist.add_node(1)
llist.add_node(2)
llist.add_node(3)
llist.add_node(4)
llist.add_node(5)

n = 3 
result = llist.find_nth_node_from_end(n)
if result:
    print(f"The {n}th node from the end is: {result}")
else:
    print("Invalid input or node not found.")
