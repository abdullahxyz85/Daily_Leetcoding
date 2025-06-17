class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        
        # Calculate the possible minimum score after applying the operation
        score = max_val - min_val - 2 * k
        
        # If score is negative, it means we can make all elements equal or overlap
        return max(0, score)