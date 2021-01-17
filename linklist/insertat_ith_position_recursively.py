class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) + "-->", end="")
        head = head.next
    print("None")
def lengthofLL(head):
    cnt=0
    while head is not None:
        cnt+=1
        head=head.next
    return cnt
def insertat_ith_position(head,i,data):
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return  newNode
    if i<0:
        return head
    if head is None:
        return None
    smallHead=insertat_ith_position(head.next,i-1,data)
    head.next=smallHead
    return head
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
head = takeInput()
printLL(head)
head=insertat_ith_position(head,1,9)
printLL(head)
head=insertat_ith_position(head,0,91)
printLL(head)
