class Solution:
    def maxProduct(self, n: int) -> int:
        result = []
        while n > 0:
            digit = n % 10
            result.append(digit)
            n //= 10
        
        max_product = 0
        for i in range(len(result)):
            for j in range(i+1, len(result)):
               product = result[i] * result[j]
               if product > max_product:
                    max_product = product
        return  max_product