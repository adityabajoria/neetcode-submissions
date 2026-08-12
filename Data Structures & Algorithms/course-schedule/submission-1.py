class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = set()
        path = set()

        for i in range(numCourses):
            adj[i] = []
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        def dfs(src) -> bool:
            if src in path:
                return False
            
            if src in visited:
                return True
            
            path.add(src)

            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            
            path.remove(src)
            visited.add(src)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            
