class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod = prod * num
        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        elif prod == 0:
            return 0