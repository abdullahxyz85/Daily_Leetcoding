class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        for i in range(len(nums)):
            num = nums[nums[i]]
            ans.append(num)
        return ans