#Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:return head
        before_head=None
        before_tail=None
        after_head=None
        after_tail=None
        while head:
            if head.val<x:
                if not before_head:
                    before_head=head
                    before_tail=head
                else:
                    before_tail.next=head
                    before_tail=before_tail.next
            else:
                if not after_head:
                    after_head=head
                    after_tail=head
                else:
                    after_tail.next=head
                    after_tail=after_tail.next
            head=head.next
        if after_tail:
            after_tail.next=None
        if before_head:
            before_tail.next=after_head
            return before_head
        return after_head