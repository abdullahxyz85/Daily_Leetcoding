class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        nums = [num for row in grid for num in row]  # Flatten the grid
        
        count = Counter(nums)  # Count occurrences of each number
        
        a = b = -1  # Initialize variables for repeated and missing numbers
        for num in range(1, n * n + 1):
            if count[num] == 2:
                a = num  # Repeating number
            elif count[num] == 0:
                b = num  # Missing number
        
        return [a, b]
