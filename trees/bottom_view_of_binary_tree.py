import queue
from collections import defaultdict,OrderedDict
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
def vertical_order_traversal_util(root,dict,level):
    if root is None:
        return
    dict[level].append(root.data)
    vertical_order_traversal_util(root.left,dict,level-1)
    vertical_order_traversal_util(root.right,dict,level+1)
    return dict
def vertical_order_traversal(root):
    dic=defaultdict(list)
    level=0
    ans=vertical_order_traversal_util(root,dic,level)
    sorted_dict=[]
    for i in sorted(ans):
        sorted_dict.append(ans[i])
    return sorted_dict
def top_view(root):
    list=vertical_order_traversal(root)
    ans=[]
    for i in list:
        ans.append(i[len(i)-1])
    return ans
root=levelwise_input()
print(top_view(root))

