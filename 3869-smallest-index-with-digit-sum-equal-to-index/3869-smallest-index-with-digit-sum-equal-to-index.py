class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = 0
            temp = nums[i]
            while temp > 0:
                digit = temp % 10
                digit_sum += digit
                temp //= 10
            if digit_sum == i:
                return i
        return -1
