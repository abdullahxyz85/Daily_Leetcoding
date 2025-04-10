class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        result = []
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                if nums[i] > nums[i - k] and nums[i] > nums[i + k]:
                    result.append(nums[i])
            elif i - k < 0 and i + k >= len(nums):
                result.append(nums[i])
            elif i - k < 0:
                if nums[i] > nums[i + k]:
                    result.append(nums[i])
            elif i + k >= len(nums):
                if nums[i] > nums[i - k]:
                    result.append(nums[i])
        total_sum = sum(result)
        return total_sum
