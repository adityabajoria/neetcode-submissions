# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countgoodnodes(node, max_so_far):
            current = 0
            if not node:
                return 0
            
            if node.val >= max_so_far:
                current = 1
                max_so_far = node.val
            
            left = countgoodnodes(node.left, max_so_far)
            right = countgoodnodes(node.right, max_so_far)

            return current + left + right
        
        return countgoodnodes(root, root.val)