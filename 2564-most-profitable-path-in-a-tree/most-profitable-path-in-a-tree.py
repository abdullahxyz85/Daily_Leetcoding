from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        # Step 1: Build the adjacency list representation of the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Step 2: Determine Bob's arrival time at each node
        bob_time = {}  # Stores the time at which Bob reaches each node

        def find_bob_path(node, parent, time):
            """ Find Bob's path to node 0 and record arrival times. """
            bob_time[node] = time
            if node == 0:  # If Bob reaches root, stop recursion
                return True
            for neighbor in tree[node]:
                if neighbor != parent and find_bob_path(neighbor, node, time + 1):
                    return True
            del bob_time[node]  # Remove node if it's not on Bob's path
            return False

        find_bob_path(bob, -1, 0)

        # Step 3: DFS for Alice to find the most profitable path
        max_income = float('-inf')

        def dfs(node, parent, time, income):
            """ DFS to find the maximum income Alice can earn. """
            nonlocal max_income
            
            # Determine income at the current node
            if node in bob_time:
                if bob_time[node] > time:  # Alice arrives first
                    income += amount[node]
                elif bob_time[node] < time:  # Bob arrives first
                    pass  # Alice gets nothing
                else:  # Both arrive at the same time
                    income += amount[node] // 2
            else:
                income += amount[node]

            # If this is a leaf node, update max_income
            is_leaf = True
            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    dfs(neighbor, node, time + 1, income)

            if is_leaf:
                max_income = max(max_income, income)

        # Start DFS from the root node (Alice starts at node 0)
        dfs(0, -1, 0, 0)

        return max_income
