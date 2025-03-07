class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        # Step 1: Use the Sieve of Eratosthenes to find all primes up to `right`
        limit = right + 1
        is_prime = [True] * (limit)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, isqrt(limit) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False
        
        # Step 2: Collect prime numbers in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        # Step 3: Find the closest prime pair
        if len(primes) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        ans = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                ans = [primes[i], primes[i + 1]]
        
        return ans

