class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        for i in range(n):
            if nums[i] in mp:
                prev_index = mp[nums[i]]
                if i - prev_index <= k:
                    return True
            mp[nums[i]] = i
        return False