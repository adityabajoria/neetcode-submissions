import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles)
        left = 1
        right = max(sorted_piles)
        res = right
        while left <= right:
            total = 0
            k = (left+right) // 2
            for i in range(len(sorted_piles)):
                total += math.ceil(sorted_piles[i] / k)
            if total <= h:
                res = k
                right = k - 1
            elif total > h:
                left = k + 1
            else:
                return k
        return res

