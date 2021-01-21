class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))
def isbalance(root):
    if root is None:
        return True
    leftheight=height(root.left)
    rightheight=height(root.right)
    if leftheight-rightheight>1 or rightheight-leftheight>1:
        return False
    if isbalance(root.left) and isbalance(root.right):
        return True
    else:
        return False
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
print(isbalance(bt1))