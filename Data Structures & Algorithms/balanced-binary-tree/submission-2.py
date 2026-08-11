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
            balanced = abs(left_height - right_height) <= 1 and (left_balanced and right_balanced)
            return current_height, balanced
        
        root_height, root_balanced = height(root)
        return root_balanced