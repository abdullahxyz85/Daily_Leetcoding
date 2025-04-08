class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums) 
         
        base = list(range(1, n)) + [n, n]

        return sorted(nums) == sorted(base)