class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):  # Fix 1: loop from 1 to n
            if i % 3 == 0:
                total += i
            elif i % 5 == 0:
                total += i
            elif i % 7 == 0:       # Fix 2: check for 7 instead of n
                total += i
        return total
