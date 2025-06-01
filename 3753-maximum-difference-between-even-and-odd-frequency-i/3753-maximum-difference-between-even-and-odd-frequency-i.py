class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        odd_Num = []
        even_Num = []

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for count in freq.values():
            if count % 2 == 0:
                even_Num.append(count)
            else:
                odd_Num.append(count)

        if len(odd_Num) == 0 or len(even_Num) == 0:
            return -1

        max_diff = -1000  

        for odd in odd_Num:
            for even in even_Num:
                diff = odd - even  
                if diff > max_diff:
                    max_diff = diff  

        return max_diff
