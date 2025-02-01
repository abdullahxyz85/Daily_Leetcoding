class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # If the array has only one element, it is special
        if len(nums) == 1:
            return True
        
        # Iterate through the array and check adjacent pairs
        for i in range(len(nums) - 1):
            # Check if the parity of nums[i] and nums[i+1] is the same
            if (nums[i] % 2) == (nums[i + 1] % 2):
                return False
        
        # If all pairs have different parity, return True
        return True