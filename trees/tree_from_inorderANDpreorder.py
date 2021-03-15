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
def buildTreeFromInorderAndPreorder(pre,inorder):
    if len(pre) ==0:
        return None
    rootData=pre[0]
    root=BinaryTreeNode(rootData)
    rootNode=BinaryTreeNode(rootData)
    rootIndexInInorder=-1
    for i in range(0,len(inorder)):
        if inorder[i]==rootData:
            rootIndexInInorder= i
            break
    leftInorder=inorder[0:rootIndexInInorder]
    rightInorder=inorder[rootIndexInInorder+1:]

    lenLeftSubtree=len(leftInorder)

    leftPreorder = pre[1:lenLeftSubtree+1]
    rightPreorder = pre[lenLeftSubtree + 1:]

    leftchild=buildTreeFromInorderAndPreorder(leftPreorder,leftInorder)
    rightchild=buildTreeFromInorderAndPreorder(rightPreorder,rightInorder)

    root.left=leftchild
    root.right=rightchild

    return root
root=buildTreeFromInorderAndPreorder([1,2,4,5,3,6,7],[4,2,5,1,6,3,7])
printTreeDetailed(root)


