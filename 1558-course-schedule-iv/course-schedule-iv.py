class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Initialize reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Step 2: Mark direct prerequisites
        for pre, course in prerequisites:
            reachable[pre][course] = True
        
        # Step 3: Apply Floyd-Warshall Algorithm to find indirect prerequisites
        for k in range(numCourses):  # Intermediate node
            for i in range(numCourses):  # Start node
                for j in range(numCourses):  # End node
                    if reachable[i][k] and reachable[k][j]:  # i -> k -> j
                        reachable[i][j] = True
        
        # Step 4: Answer queries in O(1) time
        return [reachable[u][v] for u, v in queries]
