class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        
        # Check every number from 1 to the smaller of a and b
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:  # if i divides both a and b
                count += 1
        return count