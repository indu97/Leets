# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, h) -> int:
        if node is None:
            return h
        else:
            return max(self.helper(node.left, h), self.helper(node.right, h)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)