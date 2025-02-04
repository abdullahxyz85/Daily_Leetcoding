class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]  # Initialize max sum
        current_sum = nums[0]

        for i in range(1, len(nums)):  # Traverse the array from index 1
            if nums[i] > nums[i - 1]:  # If the sequence is increasing
                current_sum += nums[i]  # Add to current sum
            else:  # If the sequence breaks
                max_sum = max(max_sum, current_sum)  # Update max_sum
                current_sum = nums[i]  # Start new subarray
            
        return max(max_sum, current_sum)  # Ensure final update after the loop
    
                        