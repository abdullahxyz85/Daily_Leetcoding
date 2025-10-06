class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # n = 2
        for a in range(1, n):
            b = n - a  # b = 2 - 1
            # a = 1, b = 1
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]




    