# class Solution:
#     def isHappy(self, n: int) -> bool:
#         if n < 10:
#             return False
#         while n > 10:
#             sum_sqr_digits = 0
#             while n > 0:
#                 sum_sqr_digits += (n % 10) ** 2
#                 n //= 10
#         if sum_sqr_digits == 1:
#             return True

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            sum_sqr_digits = 0
            while n > 0:
                sum_sqr_digits += (n % 10) ** 2
                n //= 10
            n = sum_sqr_digits
        
        return n == 1
