from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            visit.add((r, c))

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] == "1"):
                        visit.add((nr, nc))
                        queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands