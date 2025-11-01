# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if head != None:
            curr = head.next
        else: 
            return head
        while(curr != None):
            if curr.val == prev.val:
                # delete the curr
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head


