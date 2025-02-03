class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        s = list(s)  # Convert string to list for modification
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in alphabets:
                i += 1
            elif s[j] not in alphabets:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
