from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i, num in enumerate(nums):
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        for c in my_dict.values():
            if c > 1:
                return True
        return False