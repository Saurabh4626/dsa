import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.right,x)

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

def levelwise_input():
    q=queue.Queue()
    print("enter root")
    rootData=int(input())
    if (rootData == -1):  ##this means user wants empty tree
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node=q.get()
        print("enter left nodes of {current_node} "
              " If no node of this "
              "then enter -1".format(current_node=current_node.data))
        left_node_data=int(input())
        if left_node_data !=-1:
            left_node = BinaryTreeNode(left_node_data)
            current_node.left=left_node
            q.put(left_node)
        print("enter right nodes of {current_node} "
              " If no node of this "
              "then enter -1".format(current_node=current_node.data))
        right_node_data = int(input())
        if right_node_data != -1:
            right_node = BinaryTreeNode(right_node_data)
            current_node.right = right_node
            q.put(right_node)
    return root

root=levelwise_input()
printTreeDetailed(root)
print(search(root,17))
print(search(root,77))