class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            bit = n % 2
            result = result * 2 + bit
            n = n // 2
        return result