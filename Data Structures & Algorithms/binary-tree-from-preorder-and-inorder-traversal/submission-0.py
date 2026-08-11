# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)

        left_inorder = inorder[:idx]
        right_inorder = inorder[idx+1:]
        left_preorder = preorder[1:idx+1]
        right_preorder = preorder[idx+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root