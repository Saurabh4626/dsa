class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def PostOrder(root):
    if root is None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data)

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
PostOrder(bt1)