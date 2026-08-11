# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def findSum(node, rem):
            if not node:
                return False
            elif not node.left and not node.right:
                return node.val == rem
            
            rem -= node.val

            left = findSum(node.left, rem)
            right = findSum(node.right, rem)

            return left or right
        
        return findSum(root, targetSum)