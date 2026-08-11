class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        mx = -1
        my_dict = {}
        for i, num in enumerate(nums):
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
            
        for key, value in my_dict.items():
            if value == 1:
                mx = max(mx, key)
        return mx