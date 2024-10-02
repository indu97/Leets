# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(l, r):
            if l is not None and r is not None:
                if l.val == r.val:
                    return helper(l.left, r.right) and helper(l.right, r.left)
                else:
                    return False
            elif l is None and r is None:
                return True
            else:
                return False
        return helper(root.left, root.right)
        