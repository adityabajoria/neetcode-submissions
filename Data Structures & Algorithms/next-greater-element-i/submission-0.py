class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        next_greatest = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                old = stack.pop()
                next_greatest[old] = num
            
            stack.append(num)

        while stack:
            old = stack.pop()
            next_greatest[old] = -1
        
        for num in nums1:
            ans.append(next_greatest[num])
        
        return ans
        


