class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for count in freq.values():
            if count > 1:   
                is_prime = True
                for i in range(2, int(count**0.5) + 1):
                    if count % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    return True

        return False
