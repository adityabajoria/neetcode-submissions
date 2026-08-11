class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2
            missing = nums[mid] - nums[0] - mid
            if missing < k:
                l = mid + 1
            elif missing >= k:
                r = mid - 1
        
        r_missing = nums[r] - nums[0] - r
        rem = k - r_missing
        return nums[r] + rem