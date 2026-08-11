class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        next_greatest = {}

        for num in nums2:
            while stack and stack[-1] < num:
                pop = stack.pop()
                next_greatest[pop] = num
            stack.append(num)
        
        while stack: # elements that weren't popped.
            pop = stack.pop()
            next_greatest[pop] = -1
        
        for n in nums1:
            ans.append(next_greatest[n])
        
        return ans