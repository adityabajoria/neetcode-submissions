class Solution:
    def findMin(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)
        minimum_val = sorted_arr[0]
        return minimum_val