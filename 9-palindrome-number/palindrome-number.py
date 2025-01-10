class Solution:
    def isPalindrome(self, x: int) -> bool:
            # Convert the integer to a string
            x_str = str(x)
            
            # Initialize an empty string to store the reversed result
            reversed_str = ""
            
            # Reverse the string using a loop
            for char in x_str:
                reversed_str = char + reversed_str  # Add each character at the beginning
            
            # Check if the reversed string is equal to the original string
            return x_str == reversed_str


        