class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        max_ones = 0
        zeros = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
        
            max_ones = max(max_ones, j - i + 1)
        return max_ones
