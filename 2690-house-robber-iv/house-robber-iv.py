class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)

        def canRob(mid):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1  # Skip adjacent house
                i += 1  # Move to next house
            return count >= k

        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid  # Try to minimize capability
            else:
                left = mid + 1  # Increase capability
        return left
