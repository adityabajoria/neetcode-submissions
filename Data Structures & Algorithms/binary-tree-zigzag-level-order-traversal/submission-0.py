# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])

        level_count = 0
        while queue:
            levels = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                levels.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            level_count += 1
            
            ans.append(levels[::-1] if level_count % 2 == 0 else levels)
        
        return ans