class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        num = 1  # Start with the smallest available digit
        
        for ch in pattern + 'I':  # Append 'I' to handle the last group
            stack.append(str(num))
            num += 1
            
            if ch == 'I':
                while stack:
                    result += stack.pop()
        
        return result
