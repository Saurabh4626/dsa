class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) + "-->", end="")
        head = head.next
    print("None")


def remove_dup_from_LL(head):
    if head is None:
        return head
    temp=head
    while temp.next is not None:
        if temp.data==temp.next.data:
            temp.next=temp.next.next
        else:
            temp=temp.next
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
head=remove_dup_from_LL(head)
printLL(head)
