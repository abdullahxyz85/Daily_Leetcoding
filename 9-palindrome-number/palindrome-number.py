class Solution:
    def isPalindrome(self, x: int) -> bool:
            x_str = str(x)
            
            reversed_str = ""
            
            for char in x_str:
                
                reversed_str = char + reversed_str  
            
            return x_str == reversed_str


        