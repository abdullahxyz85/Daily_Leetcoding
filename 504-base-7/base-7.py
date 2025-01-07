class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0:
            return "0"
        
        result = ""
        is_negative = num < 0
        num = abs(num)
        
        while(num > 0):
            result = str(num % 7) + result
            num //= 7
        
        if(is_negative):
            return "-" + result
        return result
        