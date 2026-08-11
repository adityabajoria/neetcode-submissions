class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = 1
            else:
                mp[num] += 1
        
            if mp[num] > 1:
                return True
        return False