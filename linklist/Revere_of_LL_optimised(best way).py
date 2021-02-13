##time complexity of previous code was O(n*n)
##complexity of this code is O(n)
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

def reverseofLL(head):
    if head is None or head.next is None:
        return head
    small_head=reverseofLL(head.next)   ##get head of smaller part of LL
    tail=head.next
    tail.next=head
    head.next=None
    return small_head

head = takeInput()
printLL(head)
head=reverseofLL(head)
printLL(head)