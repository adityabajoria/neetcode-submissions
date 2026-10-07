import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        mp = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        
        for num, count in mp.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for count, num in heap:
            res.append(num)
        
        return res