import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        
        # Directions: 1 -> right, 2 -> left, 3 -> down, 4 -> up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (row, col) for right, left, down, up
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0, 0)]  # (cost, row, col)
        
        # Cost grid initialized to infinity
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        
        # Helper function to check if a cell is within bounds
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        while pq:
            curr_cost, r, c = heapq.heappop(pq)
            
            # If we reach the bottom-right corner, return the cost
            if r == m - 1 and c == n - 1:
                return curr_cost
            
            # Current direction from grid[r][c]
            grid_direction = grid[r][c] - 1
            
            # Explore 4 possible directions (right, left, down, up)
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                new_cost = curr_cost + (1 if i != grid_direction else 0)
                
                if isValid(nr, nc) and new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
        
        # If there's no valid path
        return -1