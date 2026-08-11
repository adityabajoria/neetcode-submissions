class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        for i, value in enumerate(nums2):
            my_dict[value] = i
        
        ans = []
        for i, result in enumerate(nums1):
            if result in my_dict:
                ans.append(my_dict[result])
        return ans