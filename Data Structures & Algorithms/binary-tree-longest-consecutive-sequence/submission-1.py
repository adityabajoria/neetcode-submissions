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
            length = 1
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left is not None and node.left.val == node.val + 1:
                length = max(length, 1 + left)
            
            if node.right is not None and node.right.val == node.val + 1:
                length = max(length, 1 + right)
            
            self.res = max(self.res, length)
            return length
        
        dfs(root)
        return self.res
