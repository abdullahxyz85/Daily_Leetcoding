from collections import deque, defaultdict
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Find connected components and check bipartiteness
        color = {}  # For bipartite check
        components = []  # Store connected components

        def bfs_check(start):
            queue = deque([start])
            color[start] = 0  # Start coloring with 0
            component = {start}

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in color:
                        if color[neighbor] == color[node]:  # Conflict found, odd-length cycle
                            return False, None
                    else:
                        color[neighbor] = 1 - color[node]  # Alternate colors
                        queue.append(neighbor)
                        component.add(neighbor)

            components.append(component)
            return True, None

        # Traverse all nodes to find components
        for node in range(1, n + 1):
            if node not in color:
                valid, _ = bfs_check(node)
                if not valid:
                    return -1  # If not bipartite, return -1

        # Step 3: Compute max BFS depth in each component
        def bfs_max_depth(start):
            queue = deque([start])
            visited = {start}
            depth = 0

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                depth += 1  # Increment depth for each BFS level

            return depth

        max_groups = 0
        for component in components:
            max_depth = 0
            for node in component:
                max_depth = max(max_depth, bfs_max_depth(node))
            max_groups += max_depth

        return max_groups
