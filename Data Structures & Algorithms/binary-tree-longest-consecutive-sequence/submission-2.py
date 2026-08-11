# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return 0
            
            current_length = 1
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val + 1:
                current_length = max(current_length, 1 + left)
            
            if node.right and node.right.val == node.val + 1:
                current_length = max(current_length, 1 + right)
            
            self.res = max(self.res, current_length)
            
            return current_length
        
        dfs(root)
        return self.res