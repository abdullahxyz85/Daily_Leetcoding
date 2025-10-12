class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)
        for x in range(n + 1):  # x = 0
            count = 0
            for num in nums:
                if num >= x:
                    count += 1

            if count == x:  # 0 == 0
                return x

        return -1
