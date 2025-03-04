class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat_value = 0  
        left, right = 0, len(nums) - 1
        
        while left <= right:
            if left == right:
                concat_value += nums[left]
            else:
                concat_value += int(str(nums[left]) + str(nums[right]))
            
            left += 1
            right -= 1 
        
        return concat_value


# from typing import List

# class Solution:
#     def findTheArrayConcVal(self, nums: List[int]) -> int:
#         total = 0
#         while nums:
#             if len(nums) == 1:
#                 total += nums.pop()
#             else:
#                 first = nums.pop(0)  # Remove first element
#                 last = nums.pop(-1)  # Remove last element
#                 total += int(str(first) + str(last))  # Concatenate and add
#         return total
