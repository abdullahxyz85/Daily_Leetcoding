from collections import deque
from typing import List

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list
        adj = [[] for _ in range(n)]
        # indegree array
        indegree = [0] * n
        ans = []

        # build the graph
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)   # edge prerequisite -> course
            indegree[course] += 1              # increase indegree of course

        # queue for courses with no prerequisites
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # BFS
        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1     # one prerequisite removed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # if we managed to take all courses, return True
        return len(ans) == n