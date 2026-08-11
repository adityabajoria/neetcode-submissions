# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = {}
        ans = []
        if not root:
            return ans
        
        queue = deque([(root, 0)])

        while queue:
            for _ in range(len(queue)):
                curr, col = queue.popleft()
                if curr.left is not None:
                    queue.append((curr.left, col-1))
                if curr.right is not None:
                    queue.append((curr.right, col+1))
                if col not in mp:
                    mp[col] = []
                mp[col].append(curr.val)
        
        for col in sorted(mp):
            ans.append(mp[col])
        return ans
            