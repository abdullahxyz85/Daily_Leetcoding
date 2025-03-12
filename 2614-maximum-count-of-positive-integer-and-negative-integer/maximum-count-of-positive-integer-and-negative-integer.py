class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_count = bisect_left(nums, 0)  # First non-negative index (first zero or positive)
        pos_count = len(nums) - bisect_left(nums, 1)  # First positive index
        return max(neg_count, pos_count)