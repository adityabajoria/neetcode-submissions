# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            self.count -= 1
            if self.count == 0:
                return node.val
            right = dfs(node.right)

            if left is not None:
                return left
            
            if right is not None:
                return right
        
        return dfs(root)