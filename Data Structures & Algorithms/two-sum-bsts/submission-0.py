# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return
            seen.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        def check(node):
            if not node:
                return False
            
            complement = target - node.val
            if complement in seen:
                return True
            
            return check(node.left) or check(node.right)
        
        dfs(root1)
        return check(root2)