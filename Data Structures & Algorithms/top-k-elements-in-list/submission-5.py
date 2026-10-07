class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mp = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        
        sorted_values = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            res.append(sorted_values[i][0])
        
        return res