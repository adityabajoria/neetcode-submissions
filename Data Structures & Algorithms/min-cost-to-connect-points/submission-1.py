import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                weights = abs(x1 - x2) + abs(y2 - y1)
                adj[i].append((j, weights))
                adj[j].append((i, weights))
        
        minHeap = []
        total_cost = 0

        for neighbor, weight in adj[0]:
            heapq.heappush(minHeap, [weight, 0, neighbor])
        
        visit = {0}

        while len(visit) < n:
            w1, n1, n2 = heapq.heappop(minHeap)
            if n2 in visit:
                continue
            
            total_cost += w1
            visit.add(n2)

            for neighbor, weight in adj[n2]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, n2, neighbor])
        
        return total_cost 

