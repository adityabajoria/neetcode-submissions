class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # invalid conditions
            if (r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))

            area = 1

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)
        
        return max_area