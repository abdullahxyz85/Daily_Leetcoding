class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        treshold = len(arr) // 4
        for key, values in freq.items():
            if values > treshold:
                return key