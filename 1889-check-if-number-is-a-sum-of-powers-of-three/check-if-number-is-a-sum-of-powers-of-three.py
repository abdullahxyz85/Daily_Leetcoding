class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:  # If any digit in base-3 representation is '2', return False
                return False
            n //= 3  # Reduce n by dividing it by 3
        return True
