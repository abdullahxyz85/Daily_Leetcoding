from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_value = 0  # Initialize the concatenation value
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if left == right:
                # Only one element left in the array
                concat_value += nums[left]
            else:
                # Concatenate first and last elements as strings, then convert back to integer
                concat_value += int(str(nums[left]) + str(nums[right]))
            
            left += 1
            right -= 1  # Move pointers inward
        
        return concat_value
