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

def merge_two_sorted_LL(head1,head2):
    ##first comparing both LL and setting variable finalhead and finaltail
    ## as min of both heads of LL
    ##after that just we r comparing head of LL and and go on adding to tail of
    ## LL and increasing tail to tail.next
    final_tail=Node(head2.data) if(head1.data>head2.data) else Node(head1.data)

    if head2.data > head1.data:
        head1=head1.next
    else:
        head2=head2.next
    final_head=final_tail
    while(head1 != None and head2 != None):
        if head2.data < head1.data:
            newNode=Node(head2.data)
            final_tail.next=newNode
            final_tail=final_tail.next
            head2 = head2.next
        else:
            newNode = Node(head1.data)
            final_tail.next = newNode
            final_tail=final_tail.next
            head1 = head1.next
    if (head1 != None):
        newNode = head1
        final_tail.next = newNode
    if (head2 != None):
        newNode = head2
        final_tail.next = newNode
    return final_head




print("Enter first sorted LinkList")
head1 = takeInput()
print("Enter second sorted LinkList")
head2 = takeInput()
printLL(head1)
printLL(head2)
final_head=merge_two_sorted_LL(head1,head2)
printLL(final_head)