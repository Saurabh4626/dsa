# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lengthofLL(self, head):
        cnt = 0
        while head is not None:
            cnt += 1
            head = head.next
        print(cnt)
        return cnt

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        a = head
        b = head
        len = self.lengthofLL(head)
        if len == 1:
            return None
        x = len - n
        if x == 0: return head.next
        while count != x:
            a = b
            b = b.next
            count += 1
        a.next = b.next
        return head


