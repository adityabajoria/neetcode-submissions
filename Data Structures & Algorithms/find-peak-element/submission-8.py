class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2
            if mid > 0 and mid < n-1:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] > nums[mid]:
                    r = mid - 1
                elif nums[mid+1] > mid:
                    l = mid + 1
            elif mid == 0:
                if nums[0] > nums[1]:
                    return 0
                else:
                    l = mid + 1
            elif mid == n-1:
                if nums[n-1] > nums[n-2]:
                    return n-1
                else:
                    r = mid - 1
