# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        candidates = [root]
        lowest = None
        while candidates:
            n = candidates.pop()
            if not n:
                continue
            elif self.isSubtree(n, p) and self.isSubtree(n, q):
                lowest = n
            candidates.extend([n.left, n.right])
        return lowest

    def isSubtree(self, root, p):
        if self.isSame(root, p):
            return True
        elif not root:
            return False
        else:
            return self.isSubtree(root.left, p) or self.isSubtree(root.right, p)

    def isSame(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
