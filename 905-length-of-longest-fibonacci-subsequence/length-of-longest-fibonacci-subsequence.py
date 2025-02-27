from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr):
        index_map = {num: idx for idx, num in enumerate(arr)}
        dp = defaultdict(lambda: 2)  # Default length is 2 (at least two elements needed)
        max_len = 0
        
        for j in range(1, len(arr)):
            for i in range(j):
                prev = arr[j] - arr[i]
                
                if prev < arr[i] and prev in index_map:
                    k = index_map[prev]
                    dp[(i, j)] = dp[(k, i)] + 1
                    max_len = max(max_len, dp[(i, j)])
        
        return max_len if max_len >= 3 else 0
