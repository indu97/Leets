# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def round2(self, head: Optional[ListNode], fast: ListNode):
        slow = head 
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return fast
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            if fast.next != None: 
                fast = fast.next.next
            else: 
                return None
            if slow == fast:
                return self.round2(head, fast)
        return None
        