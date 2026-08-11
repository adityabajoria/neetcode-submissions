class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
            
            if mp[nums[i]] > 1:
                return True
        return False