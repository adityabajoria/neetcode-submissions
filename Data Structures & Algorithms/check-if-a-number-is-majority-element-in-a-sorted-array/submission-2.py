class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = nums.count(target)
        majority_ele = len(nums) / 2
        return True if count > majority_ele else False 