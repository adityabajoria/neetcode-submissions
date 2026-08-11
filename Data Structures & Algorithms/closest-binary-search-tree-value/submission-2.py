# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return
        
        left = self.closestValue(root.left, target)
        right = self.closestValue(root.right, target)
        
        if root.val < target:
            child = right
        elif root.val > target:
            child = left
        else:
            child = root.val
        
        if child is None:
            return root.val
        
        if abs(root.val - target) <= abs(child - target):
            return root.val
        else:
            return child