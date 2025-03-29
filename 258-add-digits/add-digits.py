class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10: 
            sum_digits = 0 # 1 + 1 = 2
            while num > 0: # 8 > 0
                sum_digits += num % 10 
                num //= 10  
            num = sum_digits  
        return num


        # if num == 0:
        #     return 0
        # sum_digits = 0, # 8 + 3 = 11 + 1 + 1
        # while num < 10:
        #     sum_digits += num % 10
        #     num //= 10
        # num = sum_digits

