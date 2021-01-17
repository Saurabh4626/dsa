class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) + "-->", end="")
        head = head.next
    print("None")
def reverseLL(head):
    if head is None or head.next is None:
        return head
    smallhead=reverseLL(head)
    curr=smallhead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallhead
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
head=reverseLL(head)
printLL(head)

