# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree_values = []
        level = [root]
        while level:
            level_values = []
            next_level = []
            for n in level:
                if n:
                    level_values.append(n.val)
                    next_level.extend([n.left, n.right])
            
            if level_values:
                tree_values.append(level_values)
            level = next_level
        
        right_values = []
        for level_values in tree_values:
            right_values.append(level_values[-1])
        return right_values
