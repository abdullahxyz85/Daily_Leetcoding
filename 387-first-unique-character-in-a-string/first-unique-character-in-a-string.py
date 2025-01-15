class Solution:
    def firstUniqChar(self, s: str) -> int:
            # Create a dictionary to count the occurrences of each character
        char_count = {}
        
        # First pass: Count the frequency of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Second pass: Find the first character with a count of 1
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        
        # If no unique character is found, return -1
        return -1 