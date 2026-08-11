class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        i = 0
        count_zeros = 0
        window = []
        for j in range(len(nums)):
            window.append(nums[j])
            if nums[j] == 0:
                count_zeros += 1
            
            while count_zeros > 1:
                if nums[i] == 0:
                    count_zeros -= 1
                i += 1

            longest = max(longest, j-i+1)
        
        return longest