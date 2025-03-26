class Solution:
    def minimumSum(self, num: int) -> int:
        d1 = num // 1000      
        d2 = (num // 100) % 10  
        d3 = (num // 10) % 10  
        d4 = num % 10           

        digits = [d1, d2, d3, d4]
        
        for i in range(4):
            for j in range(i + 1, 4):
                if digits[i] > digits[j]:
                    digits[i], digits[j] = digits[j], digits[i]

        new1 = digits[0] * 10 + digits[2]  
        new2 = digits[1] * 10 + digits[3]  

        return new1 + new2
