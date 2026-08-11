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
            longest = 1
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and node.left.val - 1 == node.val:
                longest = max(longest, 1 + left)
            
            if right and node.right.val - 1 == node.val:
                longest = max(longest, 1 + right)
            
            self.res = max(self.res, longest)
            return longest
        
        dfs(root)
        return self.res