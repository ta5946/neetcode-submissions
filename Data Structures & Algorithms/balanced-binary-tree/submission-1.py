# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        balanced = abs(rd - ld) <= 1
        return balanced and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        return 1 + max(ld, rd)
