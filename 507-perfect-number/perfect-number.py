class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False  # 1 is not a perfect number

        sum_divisors = 1  # Start with 1 because every number is divisible by 1
        i = 2  # Start from 2 because 1 is already counted

        while i * i <= num:  # Only iterate up to sqrt(num)
            if num % i == 0:  # If 'i' is a divisor
                sum_divisors += i  # Add 'i'
                if i != num // i:  # Avoid counting the square root twice
                    sum_divisors += num // i  # Add its pair divisor
            i += 1  # Move to the next divisor

        return sum_divisors == num  # Check if sum equals num

