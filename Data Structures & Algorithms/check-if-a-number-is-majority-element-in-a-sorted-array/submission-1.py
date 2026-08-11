class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0
        majority_element = len(nums) / 2
        count = nums.count(target)
        if count > majority_element:
            return True
        return False