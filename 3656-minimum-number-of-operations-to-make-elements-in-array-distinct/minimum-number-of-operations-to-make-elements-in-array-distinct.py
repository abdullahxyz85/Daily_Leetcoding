class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        
        while len(nums) != len(set(nums)):  # While there are duplicates

            nums = nums[3:]
            operations += 1
        
        return operations