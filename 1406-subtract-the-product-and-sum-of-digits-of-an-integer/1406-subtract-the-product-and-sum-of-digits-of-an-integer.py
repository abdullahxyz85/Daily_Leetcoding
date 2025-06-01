class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        result = []
        while n > 0:
            last_digit = n % 10
            result.append(last_digit)
            n = n//10
        difference = prod(result) - sum(result)
        return difference