class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p_sum = 0
        count_subarrays = 0
        seen = {0: 1}

        for num in nums:
            p_sum += num

            if p_sum - k in seen:
                count_subarrays += seen[p_sum - k]
            
            if p_sum in seen:
                seen[p_sum] += 1
            else:
                seen[p_sum] = 1
            
        return count_subarrays