
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) + "-->", end="")
        head = head.next
    print("None")
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

def remove(head,val):
    prev = Node(0)
    prev.next = head
    curr = prev
    while curr and curr.next is not None:
        if curr.next.data == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return prev.next
head = takeInput()
printLL(head)
head=remove(head,4)
printLL(head)
