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
def len_of_LL(head):
    count=0
    while head is not None:
        head=head.next
        count+=1
    return count
def midElement(head):
    count=len_of_LL(head)  ##this gives us length of LL
    ## we have to traverse till count//2
    ## to get mid elemnt
    mid_element=count//2
    tempcount=0
    while tempcount<mid_element:
        head=head.next
        tempcount+=1
    return head.data
head = takeInput()
printLL(head)
print(midElement(head))