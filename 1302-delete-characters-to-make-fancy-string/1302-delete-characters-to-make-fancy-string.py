class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0  # to count consecutive same characters

        for char in s:
            if result and char == result[-1]:
                count += 1
            else:
                count = 1  # reset the count when char is different

            if count < 3:
                result.append(char)

        return ''.join(result)