class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total_sum = 0

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            for j in range(start, i + 1):
                total_sum += nums[j]

        return total_sum