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
    if i<0 or i>lengthofLL(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count=count+1
    newNode=Node(data)
    if prev is None:
        head=newNode
    else:
        prev.next=newNode
    newNode.next=curr
    return  head


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
