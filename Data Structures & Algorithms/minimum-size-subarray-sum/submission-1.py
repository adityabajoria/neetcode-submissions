class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        current_sum = 0
        min_length = float('inf')
        for j in range(0, len(nums)):
            current_sum += nums[j]
            while current_sum >= target:
                min_length = min(min_length, j-i+1)
                current_sum -= nums[i]
                i += 1
        
        if min_length == float('inf'):
            return 0
        return min_length