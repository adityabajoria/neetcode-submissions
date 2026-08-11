from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        max_area = 0
        
        def dfs(r, c):
            if (r not in range(rows) or c not in range(cols) or grid[r][c] != 1 or (r,c) in visited):
                return 0
            
            visited.add((r, c))

            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)
        return max_area