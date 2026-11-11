
class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        even = 0
        odd = 0
        index = 0

        while n > 0:
            bit = n % 2

            if bit == 1:
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1

            n = n // 2
            index += 1

        return [even, odd]
