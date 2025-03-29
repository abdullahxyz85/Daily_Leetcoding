class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # Repeat until num becomes a single digit
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10  # Extract last digit and add to sum
                num //= 10  # Remove last digit
            num = sum_digits  # Update num to the new sum
        return num