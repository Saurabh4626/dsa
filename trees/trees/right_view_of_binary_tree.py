import queue
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

def right_view(root):
    q=queue.Queue()
    res=[]
    if root is None:
        return
    q.put(root)
    while (not(q.empty())):
        level=[]
        size=q.qsize()
        while size:
            curr_node=q.get()
            level.append(curr_node.data)
            if curr_node.left:
                q.put(curr_node.left)
            if curr_node.right:
                q.put(curr_node.right)
            size-=1
        res.append(level)
    right_view=[]
    for i in res:
        right_view.append(i[len(i)-1])
    return right_view
root=levelwise_input()
print(right_view(root))

