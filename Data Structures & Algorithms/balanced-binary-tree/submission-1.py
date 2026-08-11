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
        
        def height(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = height(node.left)
            right_height, right_balanced = height(node.right)
            
            current_height = 1 + max(left_height, right_height)
            balanced = (left_balanced and right_balanced) and abs(left_height - right_height) <= 1

            return current_height, balanced
        
        height, balanced = height(root)
        return balanced # this returns a boolean