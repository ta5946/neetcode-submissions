# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.countLen(head)
        k = l - n
        if k == 0:
            return head.next
        
        previous = head
        current = head.next
        for i in range(k - 1):
            previous = current
            current = current.next

        previous.next = current.next        
        return head

    def countLen(self, head: Optional[ListNode]) -> int:
        i = 0
        current = head
        while current:
            i += 1
            current = current.next
        return i
