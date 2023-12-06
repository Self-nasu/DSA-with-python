class BTreeNode:
   def __init__(self, leaf=True):
       self.keys = []
       self.children = []
       self.leaf = leaf

   def is_leaf(self):
       return self.leaf


class BTree:
   def __init__(self, t):
       self.root = BTreeNode()
       self.t = t  # Degree of the tree

   def insert(self, value):
       root = self.root
       if len(root.keys) == (2 * self.t) - 1:
           new_root = BTreeNode(leaf=False)
           new_root.children.append(self.root)
           self.root = new_root
           self.split_child(new_root, 0)
           self.insert_non_full(new_root, value)
       else:
           self.insert_non_full(root, value)

   def insert_non_full(self, node, value):
       i = len(node.keys) - 1
       if node.is_leaf():
           node.keys.append(None)
           while i >= 0 and value < node.keys[i]:
               node.keys[i + 1] = node.keys[i]
               i -= 1
           node.keys[i + 1] = value
       else:
           while i >= 0 and value < node.keys[i]:
               i -= 1
           i += 1
           if len(node.children[i].keys) == (2 * self.t) - 1:
               self.split_child(node, i)
               if value > node.keys[i]:
                   i += 1
           self.insert_non_full(node.children[i], value)

   def split_child(self, parent, index):
       t = self.t
       child = parent.children[index]
       new_child = BTreeNode(leaf=child.is_leaf())
       parent.children.insert(index + 1, new_child)
       parent.keys.insert(index, child.keys[t - 1])
       new_child.keys = child.keys[t: (2 * t) - 1]
       child.keys = child.keys[:t - 1]
       if not child.is_leaf():
           new_child.children = child.children[t: 2 * t]
           child.children = child.children[:t]

   def preorder_traversal(self, node):
       if node:
           print(node.keys, end=" ")
           if not node.is_leaf():
               for child in node.children:
                   self.preorder_traversal(child)

   def inorder_traversal(self, node):
       if node:
           if not node.is_leaf():
               for i in range(len(node.keys) + 1):
                   self.inorder_traversal(node.children[i])
           print(node.keys, end=" ")

   def postorder_traversal(self, node):
       if node:
           if not node.is_leaf():
               for child in node.children:
                   self.postorder_traversal(child)
           print(node.keys, end=" ")


# Usage example:
if __name__ == "__main__":
   b_tree = BTree(3)  # Degree 3 for the B-Tree

   elements = [10, 20, 5, 6, 12, 30, 7, 17, 3, 9, 8]

   for element in elements:
       b_tree.insert(element)

   print("Preorder Traversal:")
   b_tree.preorder_traversal(b_tree.root)
   print("\n")

   print("Inorder Traversal:")
   b_tree.inorder_traversal(b_tree.root)
   print("\n")

   print("Postorder Traversal:")
   b_tree.postorder_traversal(b_tree.root)
   print("\n")