def printInOrder(root):
     if root:
         printInOrder(root.left)
         print(root.data)
         printInOrder(root.right)

def printPreOrder(root):
    if root:
        print(root.data)
        printPreOrder(root.left)
        printPreOrder(root.right)

def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data    

 



root = Node(10)
root.insert(8)
root.insert(20)
root.insert(3)
root.insert(25)
print("InOrder Traversal is: ")
printInOrder(root)
print("-----------------------")
print("PreOrder Traversal is:")
printPreOrder(root)
print("-----------------------")
print("PostOrder Traversal is:")
printPostOrder(root)