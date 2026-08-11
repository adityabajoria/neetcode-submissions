class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            # invalid conditions
            if (r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == "0"):
                return 0
            
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1 
        
        return islands