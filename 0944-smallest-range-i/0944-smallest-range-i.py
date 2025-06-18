class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        
        score = max_val - min_val - 2 * k
        
        return max(0, score)