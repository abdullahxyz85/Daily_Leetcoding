class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    count += 1
            else:
                if s[i] == '1':
                    count += 1

        return min(count, len(s) - count)