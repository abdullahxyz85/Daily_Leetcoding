class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ""
            for i in range(len(s) - 1):
                digit1 = int(s[i])
                digit2 = int(s[i + 1])
                sum_mod = (digit1 + digit2) % 10
                new_s += str(sum_mod)
            s = new_s
        return s[0] == s[1]