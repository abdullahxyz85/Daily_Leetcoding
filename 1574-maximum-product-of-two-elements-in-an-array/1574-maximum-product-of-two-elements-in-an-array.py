class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_Num = sorted(nums)
        
        value = (sorted_Num[-1]-1)*(sorted_Num[-2]-1)
        return value