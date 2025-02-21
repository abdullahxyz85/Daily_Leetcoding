class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0
        for i in range(len(num)):
            digits = int(num[i])
            if i % 2 == 0:
                even_sum += digits
            else:
                odd_sum += digits
        return even_sum == odd_sum