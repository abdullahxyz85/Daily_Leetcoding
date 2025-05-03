class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n <= 0): 
         return False
        while(n % 2 == 0):  # 16 % 2 == 0: 16 / 2= 8/2= 4/2 = 2/2 = 1
            n = n / 2 
        return n == 1  # 3 == 1