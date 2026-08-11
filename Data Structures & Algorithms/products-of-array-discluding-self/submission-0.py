class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(n):
                if j != i:
                    product *= nums[j]
            ans.append(product)
        return ans