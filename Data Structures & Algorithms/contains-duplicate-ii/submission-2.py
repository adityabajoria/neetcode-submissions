from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_map = Counter(nums[:k+1])
        for c in window_map.values():
            if c > 1:
                return True
        
        for i in range(0, len(nums)-k-1):
            trailing_digit = nums[i]
            leading_digit = nums[i+k+1]
            window_map[trailing_digit] -= 1
            window_map[leading_digit] += 1
            if window_map[leading_digit] > 1:
                return True
        return False