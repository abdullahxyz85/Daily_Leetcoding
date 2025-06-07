class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        encrypted = ""

        for i in range(n):
            new_index = (i + k) % n
            encrypted += s[new_index]

        return encrypted