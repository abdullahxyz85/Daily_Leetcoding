class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered_points = set()  # Use a set to store unique covered points
        
        for start, end in nums:
            for point in range(start, end + 1):  # Add all points in the range [start, end]
                covered_points.add(point)
        
        return len(covered_points)  # Return the total count of unique covered points
