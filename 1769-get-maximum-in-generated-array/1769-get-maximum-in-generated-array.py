class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        nums = [0] * (n + 1)
        
        nums[0] = 0
        nums[1] = 1
        
        for i in range(1, n + 1):  
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        
        return max(nums)
