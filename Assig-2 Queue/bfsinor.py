class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printInorder(root):

	if root:
		printInorder(root.left)
		print(root.val, end="\n"),
		printInorder(root.right)

def printpreorder(root):
    
    if root:
        print(root.val, end="\n")
        printpreorder(root.left)
        printpreorder(root.right)
        
def printpostorder(root):
    if root:
        printpostorder(root.left)
        printpostorder(root.right)
        print(root.val,end="\n")
    
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

print("\n In order is")
printInorder(root)

print("\nPre Order is")
printpreorder(root)

print("\nPost Order is")
printpostorder(root)