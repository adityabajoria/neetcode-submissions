from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    # valid cases
                    if (nr in range(rows) and nc in range(cols) and (nr, nc) not in visited and grid[nr][nc] == "1"):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands