class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        current_total = 0
        min_length = float("inf")
        for j in range(0, len(nums)):
            current_total += nums[j]
            while current_total >= target:
                min_length = min(min_length, j-i+1)
                current_total -= nums[i]
                i += 1
        if min_length == float("inf"):
            return 0
        return min_length