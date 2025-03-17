# class Solution:
#     def divideArray(self, nums: List[int]) -> bool:
#         freq = {}  
#         for num in nums:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1

#         for value in freq.values():
#             if value % 2 != 0:  
#                 return False

#         return True  
from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()  # Step 1: Sort the array (O(n log n))
        for i in range(0, len(nums), 2):  # Step 2: Check every pair
            if nums[i] != nums[i + 1]:  # Step 3: If pair is not equal, return False
                return False
        return True  # Step 4: If all pairs are valid, return True
