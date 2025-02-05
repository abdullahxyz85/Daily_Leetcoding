class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_length = 10**6  # Large number to store minimum length
        
        # Iterate with right pointer
        for right in range(len(nums)):
            current_sum += nums[right]  # Expand the window
            
            # Shrink the window from left if sum >= target
            while current_sum >= target:
                # Calculate the length manually
                length = right - left + 1  
                if length < min_length:
                    min_length = length  # Update minimum length

                current_sum -= nums[left]  # Reduce window size
                left += 1  # Move left pointer forward

        # If min_length was not updated, return 0
        if min_length == 10**6:
            return 0
        return min_length
