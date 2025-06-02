class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            digits = []  
            temp = x
            while temp > 0:
                digits.append(temp % 10)
                temp //= 10
            max_digit = max(digits)  
            encrypted_number = int(str(max_digit) * len(digits))  
            return encrypted_number

        total = 0
        for num in nums:
            total += encrypt(num)
        return total