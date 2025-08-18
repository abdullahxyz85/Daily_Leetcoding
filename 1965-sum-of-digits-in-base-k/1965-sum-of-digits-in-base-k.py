class Solution:
    def sumBase(self, n: int, k: int) -> int:
        total = 0
        while n > 0:
            remainder = n % k       
            total += remainder       
            n //= k                 
        return total