# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left is not None:
                    queue.append(curr.left)
                
                if curr.right is not None:
                    queue.append(curr.right)
                
            ans.append(level)
        
        return ans