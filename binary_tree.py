class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class binarytree:
    def __init__(self):
        self.root = None
        
    def insert_in_tree(self,data):
        if self.root is None:
            self.root = node(data)
        else:
            self.recursive_insert(self.root,data)
    
    def recursive_insert(self,main_node,data):
        if data < main_node.data:
            if main_node.left is None:
                main_node.left = node(data)
            else:
                self.recursive_insert(main_node.left,data)
        else:
            if main_node.right is None:
                main_node.right = node(data)
            else:
                self.recursive_insert(main_node.right,data)
                
    def preorder(self,node):
        if node:
            print(node.data, end="-->")
            self.preorder(node.left)
            self.preorder(node.right)
            
                
Mytree = binarytree()

elements = [9,44,8,12,29,13,43,27,36,29]
for element in elements:
    Mytree.insert_in_tree(element)

Mytree.preorder(Mytree.root)

