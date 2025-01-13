class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)  # Length of the array
        special_sum = 0

        # Iterate through all indices (1-indexed)
        for i in range(1, n + 1):
            if n % i == 0:  # Check if i divides n
                special_sum += nums[i - 1] ** 2  # Add square of the special element

        return special_sum