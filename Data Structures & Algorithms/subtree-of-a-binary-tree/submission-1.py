# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subroot):
            if not root and not subroot:
                return True
            elif not root or not subroot:
                return False
            
            left = isSame(root.left, subroot.left)
            right = isSame(root.right, subroot.right)

            return True if root.val == subroot.val and (left and right) else False
        
        same = isSame(root, subRoot)
        if not root:
            return False
        left_subtree = self.isSubtree(root.left, subRoot)
        right_subtree = self.isSubtree(root.right, subRoot)
        return same or left_subtree or right_subtree