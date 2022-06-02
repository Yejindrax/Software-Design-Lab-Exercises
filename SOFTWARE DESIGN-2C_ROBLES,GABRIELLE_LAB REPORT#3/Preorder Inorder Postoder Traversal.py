#Preorder Traversal
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):

    if root is None:
        root = BinaryTreeNode(newValue)
        return root

    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:

        root.rightChild = insert(root.rightChild, newValue)
    return root


def preorder(root):

    if root == None:
        return

    print(root.data)

    preorder(root.leftChild)

    preorder(root.rightChild)


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
print("Printing values of binary tree in preorder Traversal.")
preorder(root)

#Inorder Traversal
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):

    if root is None:
        root = BinaryTreeNode(newValue)
        return root


    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:

        root.rightChild = insert(root.rightChild, newValue)
    return root


def inorder(root):

    if root == None:
        return

    inorder(root.leftChild)

    print(root.data)

    inorder(root.rightChild)


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
print("Printing values of binary search tree in Inorder Traversal.")
inorder(root)

#Postorder Traversal
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert(root, newValue):

    if root is None:
        root = BinaryTreeNode(newValue)
        return root

    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:

        root.rightChild = insert(root.rightChild, newValue)
    return root


def postorder(root):

    if root == None:
        return

    postorder(root.leftChild)

    postorder(root.rightChild)

    print(root.data)


root = insert(None, 15)
insert(root, 10)
insert(root, 25)
insert(root, 6)
insert(root, 14)
insert(root, 20)
insert(root, 60)
print("Printing values of binary tree in postorder Traversal.")
postorder(root)