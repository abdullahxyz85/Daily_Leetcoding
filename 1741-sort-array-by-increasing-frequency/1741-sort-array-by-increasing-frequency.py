from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        result = nums.copy()  # Make a copy so we can sort in-place

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Manual bubble sort based on (freq[x], -x)
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Compare using frequency and value
                a, b = result[j], result[j + 1]
                if freq[a] > freq[b] or (freq[a] == freq[b] and a < b):
                    result[j], result[j + 1] = result[j + 1], result[j]

        return result
