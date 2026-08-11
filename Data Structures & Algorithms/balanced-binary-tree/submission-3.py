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
        def findHeight(node):
            '''
            height: returns the height (int)
            balanced: returns if tree is balanced (bool)
            '''
            if not node:
                return 0, True
            
            left_height, left_balanced = findHeight(node.left)
            right_height, right_balanced = findHeight(node.right)
            height = 1 + max(left_height, right_height)
            balanced = True if abs(left_height - right_height) <= 1 and (left_balanced and right_balanced) else False
            
            return height, balanced
        
        root_height, root_balanced = findHeight(root)
        return root_balanced

        