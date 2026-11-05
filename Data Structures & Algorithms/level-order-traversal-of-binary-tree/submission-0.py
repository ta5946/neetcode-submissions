# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree_values = []
        level = [root]
        while level:
            next_level = []
            level_values = []
            for n in level:
                if n:
                    level_values.append(n.val)
                    next_level.extend([n.left, n.right])
            
            if level_values:
                tree_values.append(level_values)
            level = next_level
        return tree_values
