class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase_len = 1  # Track length of increasing subarray
        decrease_len = 1  # Track length of decreasing subarray
        maximum_len = 1  # Store the longest subarray found

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Strictly increasing
                increase_len += 1
                decrease_len = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:  # Strictly decreasing
                decrease_len += 1
                increase_len = 1  # Reset increasing count
            else:  # If elements are equal, reset both counts
                increase_len = 1
                decrease_len = 1

            # Update the maximum found length
            maximum_len = max(maximum_len, increase_len, decrease_len)

        return maximum_len  # Return the correct value
