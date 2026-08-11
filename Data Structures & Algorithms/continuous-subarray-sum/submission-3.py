class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        p_sum = 0
        for i, num in enumerate(nums):
            p_sum += num
            rem = p_sum % k
            if rem not in mp:
                mp[rem] = i
            elif i - mp[rem] > 1:
                return True
        return False

            


        
