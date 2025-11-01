# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        curr = head.next
        while(curr != None):
            if curr.val == prev.val:
                # delete the curr
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head


