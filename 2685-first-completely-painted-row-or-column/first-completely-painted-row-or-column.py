class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pos = {}  # Mapping from value to (row, col)
        
        # Store the position of each number in mat
        for r in range(m):
            for c in range(n):
                pos[mat[r][c]] = (r, c)
        
        row_count = [0] * m  # Track painted cells in each row
        col_count = [0] * n  # Track painted cells in each column
        
        # Process arr and paint the matrix
        for i, num in enumerate(arr):
            r, c = pos[num]  # Get position of num in mat
            row_count[r] += 1
            col_count[c] += 1
            
            # Check if the entire row or column is painted
            if row_count[r] == n or col_count[c] == m:
                return i  # Return the smallest index when a row or column is fully painted
        
        return -1  # Should never reach here since a solution is guaranteed
