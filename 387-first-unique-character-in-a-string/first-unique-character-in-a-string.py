class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        # First pass: Count the occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Second pass: Find the first character with a count of 1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        # If no unique character is found, return -1
        return -1