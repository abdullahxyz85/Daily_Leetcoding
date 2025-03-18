class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer of the window
        bitmask = 0  # Stores the OR of numbers in the window
        max_length = 0  # Maximum length of nice subarray

        for right in range(len(nums)):  # Expand the window
            while (bitmask & nums[right]) != 0:  # If AND is not zero, shrink the window
                bitmask ^= nums[left]  # Remove nums[left] from the bitmask
                left += 1  # Move left pointer

            bitmask |= nums[right]  # Add nums[right] to bitmask
            max_length = max(max_length, right - left + 1)  # Update max length
        
        return max_length