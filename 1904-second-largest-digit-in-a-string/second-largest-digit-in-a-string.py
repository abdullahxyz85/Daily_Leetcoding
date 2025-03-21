class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []  

        
        for ch in s:
            if '0' <= ch <= '9': 
                num = int(ch)  
                if num not in digits:  
                    digits.append(num)
        
        if len(digits) < 2:
            return -1

    
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                if digits[i] < digits[j]: 
                    digits[i], digits[j] = digits[j], digits[i]
        
        return digits[1] 
