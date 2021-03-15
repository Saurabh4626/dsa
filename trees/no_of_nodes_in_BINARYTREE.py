class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
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
def treeinput():
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    lefttree=treeinput()
    root.left=lefttree
    righttree=treeinput()
    root.right=righttree
    return root
def NO_OF_NODES(root):
    if root is None:
        return 0
    leftnode=NO_OF_NODES(root.left)
    rightnode=NO_OF_NODES(root.right)
    return 1+leftnode+rightnode
root=treeinput()
printTreeDetailed(root)
print(NO_OF_NODES(root))