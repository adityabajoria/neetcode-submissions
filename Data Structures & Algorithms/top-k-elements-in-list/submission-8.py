import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        mp = {}
        for x in nums:
            mp[x] = mp.get(x, 0) + 1
        
        for num, freq in mp.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]