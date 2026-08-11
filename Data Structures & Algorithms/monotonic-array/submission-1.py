class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        seen_increase = False
        seen_decrease = False

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                seen_increase = True
            elif nums[i] < nums[i-1]:
                seen_decrease = True
        
        if seen_increase and seen_decrease:
            return False
        else:
            return True