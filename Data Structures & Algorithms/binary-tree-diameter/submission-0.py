class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxDepth(root)
        return self.diameter

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        self.diameter = max(self.diameter, ld + rd)
        return 1 + max(ld, rd)
