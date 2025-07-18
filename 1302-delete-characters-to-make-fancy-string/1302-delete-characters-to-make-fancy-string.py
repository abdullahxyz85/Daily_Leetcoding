class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0  

        for char in s:
            if result and char == result[-1]:
                count += 1
            else:
                count = 1 

            if count < 3:
                result.append(char)

        return ''.join(result)