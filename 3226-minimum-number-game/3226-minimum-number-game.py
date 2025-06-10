
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        for i in range(0, n, 2):
            if i + 1 < n:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
