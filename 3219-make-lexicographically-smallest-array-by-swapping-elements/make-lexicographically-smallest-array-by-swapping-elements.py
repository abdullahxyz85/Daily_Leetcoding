class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        # Step 1: Create a list of tuples (value, index)
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        
        # Step 2: Initialize the result array
        result = [0] * n
        i = 0
        
        # Step 3: Process each group of swappable numbers
        while i < n:
            j = i + 1
            # Find the end of the current swappable group
            while j < n and indexed_nums[j][0] - indexed_nums[j - 1][0] <= limit:
                j += 1
            
            # Step 4: Sort indices for this segment
            indices = sorted(indexed_nums[k][1] for k in range(i, j))
            
            # Step 5: Sort values for this segment
            values = sorted(indexed_nums[k][0] for k in range(i, j))
            
            # Step 6: Place sorted values back into result based on sorted indices
            for k in range(len(indices)):
                result[indices[k]] = values[k]
            
            # Move to next group
            i = j
        
        return result



