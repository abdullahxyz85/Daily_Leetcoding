class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            digit_sum = 0
            temp = i
            while temp  > 0:
                digit_sum += temp % 10
                temp //= 10
            if digit_sum % 2 == 0:
                count += 1
        return count