class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [] # [0, 1, 2]
        for i in range(len(nums)):
            num = nums[nums[i]]
            ans.append(num)
        return ans

        # nums[0] = 0 => nums[0] = 0
        # nums[1] = 2 => nums[2] = 1
        # nums[2] = 1 => nums[1] = 2