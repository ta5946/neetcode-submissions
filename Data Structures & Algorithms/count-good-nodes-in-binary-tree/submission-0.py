# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good_count = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.searchNodes(root, root.val)
        return self.good_count
     
    def searchNodes(self, node, max_val):
        if not node:
            return
        if node.val >= max_val:
            self.good_count += 1
            max_val = node.val
        self.searchNodes(node.left, max_val)
        self.searchNodes(node.right, max_val)
