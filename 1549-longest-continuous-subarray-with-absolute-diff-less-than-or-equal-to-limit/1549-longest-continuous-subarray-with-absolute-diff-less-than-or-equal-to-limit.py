from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        res = 0
        left = 0

        for right, num in enumerate(nums):
            while max_deque and num > max_deque[-1]:
                max_deque.pop()
            max_deque.append(num)

            while min_deque and num < min_deque[-1]:  # \U0001f527 fixed condition here
                min_deque.pop()
            min_deque.append(num)

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res