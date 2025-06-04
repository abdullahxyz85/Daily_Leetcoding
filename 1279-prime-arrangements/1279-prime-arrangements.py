class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Count prime numbers from 1 to n using inline logic (LeetCode style)
        prime_count = 0
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_count += 1

        # Calculate factorial for prime_count and (n - prime_count)
        result = 1
        for i in range(2, prime_count + 1):
            result = (result * i) % MOD
        for i in range(2, n - prime_count + 1):
            result = (result * i) % MOD

        return result
