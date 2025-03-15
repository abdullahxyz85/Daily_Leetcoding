from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            i = 0
            
            # Checking how many houses we can rob with capability `mid`
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1  # Skip the next house
                i += 1  # Move to the next house
            
            if count >= k:
                right = mid  # Try to minimize capability
            else:
                left = mid + 1  # Increase capability
        
        return left
