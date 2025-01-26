class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        # XOR all characters in both strings
        for char in s + t:
            result ^= ord(char)  # XOR the ASCII values of the characters
        return chr(result)  # Convert the resulting number back to a character

