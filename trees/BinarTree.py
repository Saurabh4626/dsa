class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 


def printTree(root):
    if root is None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetailed(root):
    if root == None:
        return
    print(root.data,end=":")
    if root.left !=None:
        print("L",root.left.data, end=",")
    if root.right !=None:
        print("R",root.right.data)
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

bt1=BinaryTreeNode(1)
bt2=BinaryTreeNode(2)
bt3=BinaryTreeNode(3)
bt4=BinaryTreeNode(7)
bt5=BinaryTreeNode(9)
bt6=BinaryTreeNode(3)
bt7=BinaryTreeNode(31)
bt1.left=bt2
bt1.right=bt3
bt2.left=bt4
bt2.right=bt5
bt3.left=bt6
bt3.right=bt7
printTreeDetailed(bt1)
