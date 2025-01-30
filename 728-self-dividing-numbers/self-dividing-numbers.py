class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        
        for num in range(left, right + 1):
            num_str = str(num)  
            is_self_dividing = True  
            
            for digit in num_str:
                if digit == '0' or num % int(digit) != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                result.append(num)
        
        return result
