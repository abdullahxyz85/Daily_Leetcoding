class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
                # Step 1: Count the set bits in num2
        count_set_bits_num2 = bin(num2).count('1')
        
        # Step 2: Generate x with the same number of set bits
        result = 0
        # Prioritize bits from num1
        for i in range(31, -1, -1):
            if count_set_bits_num2 > 0 and (num1 & (1 << i)):
                result |= (1 << i)
                count_set_bits_num2 -= 1
        
        # Add remaining set bits, starting from the least significant bit
        for i in range(32):
            if count_set_bits_num2 > 0 and not (result & (1 << i)):
                result |= (1 << i)
                count_set_bits_num2 -= 1
        
        return result