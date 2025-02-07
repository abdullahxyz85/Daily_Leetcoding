class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Take the first word as a reference
        common_chars = list(words[0])  # Convert first word to a list of characters

        # Compare with each word in the list
        for word in words[1:]:
            temp = []  # Temporary list to store common characters
            for char in common_chars:
                if char in word:  # Check if the character exists in the current word
                    temp.append(char)  # Add to temp list
                    word = word.replace(char, '', 1)  # Remove the first occurrence of char
            common_chars = temp  # Update the common characters list
        
        return common_chars

