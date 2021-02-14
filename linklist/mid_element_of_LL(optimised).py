class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data),end="--->")
        head = head.next
    print("None")
def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head

def midNode(head):
    slow=head
    fast=head
    while fast.next !=None and fast.next.next !=None:
        slow=slow.next
        fast=fast.next.next
    return slow.data

head = takeInput()
printLL(head)
print(midNode(head))