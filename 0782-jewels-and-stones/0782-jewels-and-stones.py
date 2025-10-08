class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 1. need to convert string into array.
        # 2. need to run loop
        # 3. need to check if stone is present.
        # 4. need to count.
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count