class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        my_dict = {}
        for i, val in enumerate(nums):
            if val in my_dict:
                my_dict[val] += 1
            else:
                my_dict[val] = 1
        
        sorted_values = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            ans.append(sorted_values[i][0])
        return ans