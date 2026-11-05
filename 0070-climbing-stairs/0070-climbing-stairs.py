class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}

        def dp(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = dp(n-2) + dp(n-1)
                return memo[n]
        return dp(n)