import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)  # Convert nums into a min-heap
        operations = 0
        
        while nums[0] < k:
            x = heapq.heappop(nums)  # Smallest element
            y = heapq.heappop(nums)  # Second smallest element
            
            new_val = x * 2 + y
            heapq.heappush(nums, new_val)  # Insert the new value
            
            operations += 1
        
        return operations

