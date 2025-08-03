class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            num = start + 2 * i
            result = result ^ num
        return result