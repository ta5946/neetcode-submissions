# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2
        p3 = ListNode()
        n3 = p3
        r = 0
        while n1 and n2:
            d1 = n1.val
            d2 = n2.val
            n1 = n1.next
            n2 = n2.next

            s = d1 + d2 + r
            d3 = s % 10
            r = s // 10

            n3.next = ListNode(d3)
            n3 = n3.next

        current = n1 or n2
        while current:
            s = current.val + r
            d = s % 10
            r = s // 10
            n3.next = ListNode(d)
            n3 = n3.next
            current = current.next
        
        if r:
            n3.next = ListNode(r)
        return p3.next
