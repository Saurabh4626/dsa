class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def makeBST(arr):
    if not arr:
        return None
    midelement=(len(arr))//2
    root=BinaryTreeNode(arr[midelement])
    root.left=makeBST(arr[:midelement])
    root.right=makeBST(arr[midelement+1:])
    return root
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


arr=[1,2,3,4,5,6,7]
root=makeBST(arr)
printTreeDetailed(root)
