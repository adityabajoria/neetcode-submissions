class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count_subarrays = 0
        product = 1
        if k <= product:
            return 0
        i = 0
        for j in range(len(nums)):
            product *= nums[j]

            while product >= k:
                product /= nums[i]
                i += 1
            
            count_subarrays += j - i + 1
        
        return count_subarrays