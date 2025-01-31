class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        temp = 0
        for i in range(len(nums)):
            temp = temp + nums[i]
            result.append(temp)
        return result