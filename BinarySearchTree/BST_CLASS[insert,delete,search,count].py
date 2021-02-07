class BinaryTreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
        self.numNodes=0

    ###########  PRINTING TREE #######
    def printTreeHelper(self,root):
        if root is None:
            return
        print(root.data,end=":")
        if root.left is not None:
            print("L",root.left.data,end=",")
        if root.right is not None:
            print("R",root.right.data)
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    def printTree(self):
        return self.printTreeHelper(self.root)

    ########### SEARCHING IN TREE #######
    def isPresentHelper(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        if root.data > data:
            return self.isPresentHelper(root.left, data)
        else:
            return self.isPresentHelper(root.right, data)
    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)

    ###########  INSERTING IN TREE #######
    def insertHelper(self,root,data):
        if root is None:
            node=BinaryTreeNode(data)
            return node
        if root.data>data:
            root.left=self.insertHelper(root.left,data)
            return root
        else:
            root.right=self.insertHelper(root.right,data)
            return root
    def insert(self,data):
        self.numNodes+=1
        self.root=self.insertHelper(self.root,data)

    ####### MIN OF LEFT PART OF TREE #######
    def min(self,root):
        if root is None:
            return 100000
        if root.left is None:
            return root.data
        return self.min(root.left)

    ###########  DETETING DATA IN TREE #######
    def deleteDataHelper(self,root,data):
        if root is None:
            return False,None
        if root.data<data:
            deleted,newRightNode=self.deleteDataHelper(root.right,data)
            root.right=newRightNode
            return deleted,root
        if root.data>data:
            deleted, newLefttNode = self.deleteDataHelper(root.left, data)
            root.left = newLefttNode
            return deleted, root
        ###root.data==data
        # root is leaf
        if root.left==None and root.right==None:
            return True,None

        # root has one child
        if root.left is None:
            return True,root.right
        if root.right is None:
            return True,root.left

        #root has two child
        replacement=self.min(root.right)
        root.data=replacement
        deleted,newRightNode=self.deleteDataHelper(root.right,replacement)
        root.right=newRightNode
        return True,root

    def deleteData(self,data):
        deleted,self.root=self.deleteDataHelper(self.root,data)
        if deleted:
            self.numNodes-=1
        return deleted

    ###########  TOTAL NODE IN TREE #######
    def count(self):
        return self.numNodes


b=BST()
b.insert(10)
b.insert(5)
b.insert(12)
print(b.isPresent(10))
print(b.isPresent(7))
print(b.deleteData(4))
print(b.deleteData(10))
print(b.count())
b.printTree()
