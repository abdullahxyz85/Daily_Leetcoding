class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = list(str(n))
        sum = 0
        for i in range(len(n)):
            if i % 2 == 0:
                sum += int((n[i]))
            else:
                sum -= int((n[i]))
        return sum