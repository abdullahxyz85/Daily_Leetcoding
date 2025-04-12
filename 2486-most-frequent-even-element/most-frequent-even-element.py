class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_freq = {}
        for num in nums:
            if num % 2 == 0:
               if num in even_freq:
                    even_freq[num] += 1
               else:
                    even_freq[num] = 1
        if not even_freq:
            return -1
        max_freq = 0
        result = -1
        
        for num in even_freq:
            freq = even_freq[num]
            if freq > max_freq or (freq == max_freq and num < result):
                max_freq = freq
                result = num
        
        return result