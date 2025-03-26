class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n_list = list(str(n))
        sum = 0
        for i in range(len(n_list)):
            if i % 2 == 0:
                sum += int(n_list[i])
            else:
                sum -= int(n_list[i])
        return sum