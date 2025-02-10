class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        i = 0
        
        while i < len(s):
            char = s[i]
            is_digit = '0' <= char <= '9'
            
            if is_digit:
                if len(stack) > 0:
                    stack = stack[:-1]
            else:
                stack += [char]
            
            i += 1
        
        result = ""
        for ch in stack:
            result += ch
        
        return result
