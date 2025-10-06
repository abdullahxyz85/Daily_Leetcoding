class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = {}   # {1: 1, 2: 1, 3: 2}

        for num in nums:
            if num in freq:     
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if value > 1:     
                return key
