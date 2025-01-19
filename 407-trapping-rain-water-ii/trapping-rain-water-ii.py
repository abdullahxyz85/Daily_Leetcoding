import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Step 1: Push all the boundary cells into the min-heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        # Step 2: Process cells in order of increasing height
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        trapped_water = 0

        while min_heap:
            height, x, y = heapq.heappop(min_heap)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    trapped_water += max(0, height - heightMap[nx][ny])
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True

        return trapped_water