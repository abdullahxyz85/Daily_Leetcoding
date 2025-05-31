class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        max_value = max(nums)
        min_value = min(nums)
        for i in range(len(nums)):
            if nums[i] not in (max_value, min_value):
                return nums[i]
        return -1