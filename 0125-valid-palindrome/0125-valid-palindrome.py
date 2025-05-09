class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for char in s:
            if char.isalnum():  # Check if it's a letter or digit
                cleaned += char.lower()  # Convert to lowercase and add to new string
        return cleaned == cleaned[::-1]  # Compare with its reverse
