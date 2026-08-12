class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        top_sort = []
        visited = set()
        path = set()

        for i in range(numCourses):
            adj[i] = []
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
        
        def dfs(src):
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
            top_sort.append(src)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return top_sort[::-1]