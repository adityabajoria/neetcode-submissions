# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isgoodnode(node, max_so_far):
            current = 0
            if not node:
                return False
            if node.val >= max_so_far:
                current = 1
                max_so_far = node.val
            
            left = isgoodnode(node.left, max_so_far)
            right = isgoodnode(node.right, max_so_far)

            return current + left + right
        
        return isgoodnode(root, root.val)
            