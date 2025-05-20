class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
    
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            else:
                if len(stack) == 0:
                    return False  # no matching opening bracket
                top = stack.pop()
                if ch != top:
                    return False  # mismatched bracket
        
        return len(stack) == 0  # true if all matched
