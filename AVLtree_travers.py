class Node:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
       self.height = 1

class AVLTree:
   def getHeight(self, node):
       if not node:
           return 0
       return node.height

   def getBalance(self, node):
       if not node:
           return 0
       return self.getHeight(node.left) - self.getHeight(node.right)

   def rightRotate(self, z):
       y = z.left
       T3 = y.right

       y.right = z
       z.left = T3

       z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
       y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

       return y

   def leftRotate(self, z):
       y = z.right
       T2 = y.left

       y.left = z
       z.right = T2

       z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
       y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

       return y

   def insert(self, root, data):
       if not root:
           return Node(data)
       elif data < root.data:
           root.left = self.insert(root.left, data)
       else:
           root.right = self.insert(root.right, data)

       root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

       balance = self.getBalance(root)

       if balance > 1:
           if data < root.left.data:
               return self.rightRotate(root)
           else:
               root.left = self.leftRotate(root.left)
               return self.rightRotate(root)

       if balance < -1:
           if data > root.right.data:
               return self.leftRotate(root)
           else:
               root.right = self.rightRotate(root.right)
               return self.leftRotate(root)

       return root

   def preorder_traversal(self, root):
       if root:
           print(root.data, end=" ")
           self.preorder_traversal(root.left)
           self.preorder_traversal(root.right)

   def inorder_traversal(self, root):
       if root:
           self.inorder_traversal(root.left)
           print(root.data, end=" ")
           self.inorder_traversal(root.right)

   def postorder_traversal(self, root):
       if root:
           self.postorder_traversal(root.left)
           self.postorder_traversal(root.right)
           print(root.data, end=" ")


# Usage example:
if __name__ == "__main__":
   avl_tree = AVLTree()
   root = None

   elements = [91, 51, 101, 0, 61, 111, -112, 124, 222]

   for element in elements:
       root = avl_tree.insert(root, element)

   print("Preorder Traversal:")
   avl_tree.preorder_traversal(root)
   print("\n")

   print("Inorder Traversal:")
   avl_tree.inorder_traversal(root)
   print("\n")

   print("Postorder Traversal:")
   avl_tree.postorder_traversal(root)
   print("\n")