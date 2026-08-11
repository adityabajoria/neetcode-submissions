import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            total = 0
            k = (left+right) // 2
            for i in range(len(piles)):
                total += math.ceil(piles[i] / k)
            if total <= h:
                res = k
                right = k - 1
            elif total > h:
                left = k + 1
        return res