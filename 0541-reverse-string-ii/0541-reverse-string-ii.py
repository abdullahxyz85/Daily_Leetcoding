class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        i = 0
        n = len(s)

        while i < n:
            j = 0
            temp = ""
            while j < k and i + j < n:
                temp = s[i + j] + temp  
                j += 1
            result += temp

            j = 0
            while j < k and i + k + j < n:
                result += s[i + k + j]
                j += 1

            i += 2 * k

        return result
