# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, lower_limit, upper_limit):
            if not node:
                return True
            
            if not (lower_limit < node.val < upper_limit):
                return False
            
            left = dfs(node.left, lower_limit, node.val)
            right = dfs(node.right, node.val, upper_limit)

            return left and right
        
        return dfs(root, float('-inf'), float('inf'))