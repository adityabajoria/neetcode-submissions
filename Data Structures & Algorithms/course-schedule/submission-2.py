class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visit = set()
        path = set()

        for i in range(numCourses):
            adj[i] = []
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        def dfs(src):
            if src in path:
                return False
            
            if src in visit:
                return True
            
            path.add(src)
            
            for neighbor in adj[src]:
                if not dfs(neighbor):
                    return False
            
            path.remove(src)
            visit.add(src)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True