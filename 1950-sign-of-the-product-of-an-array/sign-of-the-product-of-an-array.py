class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            x = 1
            for num in nums:
                x = x * num
            if x > 0:
                return 1
            elif x < 0:
                return -1
            elif x == 0:
                return 0

        prod = signFunc(nums)
        return prod