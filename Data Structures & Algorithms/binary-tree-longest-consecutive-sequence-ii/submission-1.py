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
            inc = 1
            dec = 1
            if not node:
                return (1, 1)
            
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)

            if node.left and node.left.val == node.val + 1:
                inc = max(inc, 1 + left_inc)
            
            if node.left and node.left.val == node.val - 1:
                dec = max(dec, 1 + left_dec)
            
            if node.right and node.right.val == node.val + 1:
                inc = max(inc, 1 + right_inc)
            
            if node.right and node.right.val == node.val - 1:
                dec = max(dec, 1 + right_dec)
            
            self.res = max(self.res, inc + dec - 1)
            
            return (inc, dec)
        
        dfs(root)
        return self.res