from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = Counter(nums)
        for c in my_dict.values():
            if c > 1:
                return True
        return False