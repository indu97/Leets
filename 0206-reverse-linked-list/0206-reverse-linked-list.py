# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  0 or 1 nodes
        if not head or not head.next:
            return head
        
        # # 2 nodes
        # if not head.next.next:
        #     head.next.next = head
        #     head = head.next
        #     head.next.next = None
        #     return head

        # More than 2 nodes
        p = head
        c = p.next
        head.next = None
        while(c is not None):
            n = c.next
            c.next = p
            p = c
            c = n

        return p