class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num)
        
        while i > 0:
            last_digit = int(num[i - 1])
            
            if last_digit % 2 != 0:
                result = ""
                for j in range(i):
                    result += num[j]
                return result
            
            i -= 1

        return ""