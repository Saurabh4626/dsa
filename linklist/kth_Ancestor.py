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

def get_path_to_node(root,node):
    if root is None:
        return None
    if root.data==node:
        return [root.data]
    if get_path_to_node(root.left,node):
        ans=get_path_to_node(root.left,node)
        ans.append(root.data)
        return ans
    if get_path_to_node(root.right,node):
        ans=get_path_to_node(root.right,node)
        ans.append(root.data)
        return ans
    return None
def kthAncestor(root,k,node):
    if root is None:
        return None
    path=get_path_to_node(root,node)
    print(path)
    if k>len(path):
        return -1
    return path[k]


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
print(kthAncestor(root,2,5))

