from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: visiting, 2: safe
        
        def dfs(node):
            if color[node]:  # If already visited
                return color[node] == 2
            
            color[node] = 1  # Mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):  # If any neighbor is not safe
                    return False
            
            color[node] = 2  # Mark as safe
            return True
        
        safe_nodes = []
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        
        return sorted(safe_nodes)

