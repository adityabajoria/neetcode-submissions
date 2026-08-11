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
            
            left_tree = isSame(root.left, subroot.left)
            right_tree = isSame(root.right, subroot.right)

            if root.val == subroot.val and (left_tree and right_tree):
                return True
            
            return False
        
        if not root:
            return False
        
        same = isSame(root, subRoot)
        left_subtree = self.isSubtree(root.left, subRoot)
        right_subtree = self.isSubtree(root.right, subRoot)
        if same:
            return True
        return left_subtree or right_subtree