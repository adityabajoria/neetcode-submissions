class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return ans