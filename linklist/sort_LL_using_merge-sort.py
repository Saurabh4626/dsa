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
    return slow
def merge(head1,head2):
    final_tail = Node(0)
    final_head=final_tail
    while (head1 != None and head2 != None):
        if head2.data < head1.data:
            final_tail.next = head2
            final_tail = final_tail.next
            head2 = head2.next
        else:
            final_tail.next = head1
            final_tail = final_tail.next
            head1 = head1.next
    while head1 is not None:
        final_tail.next=head1
        final_tail=final_tail.next
        head1=head1.next
    while head2 is not None:
        final_tail.next = head2
        final_tail = final_tail.next
        head2 = head2.next
    return final_head.next
def merge_sort(head):
    if head.next is None:
        return head
    mid_Node = midNode(head)
    head1 = head
    temp = head
    while temp is not mid_Node:
        temp=temp.next
    head2=temp.next
    temp.next=None
    head1=merge_sort(head1)
    head2=merge_sort(head2)
    return merge(head1,head2)

head = takeInput()
printLL(head)
final_head=merge_sort(head)
printLL(final_head)