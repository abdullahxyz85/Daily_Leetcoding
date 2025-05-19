
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for val in s:
            if stack:
                if stack[-1] == "A" and val =="B":
                    stack.pop()
                    continue
                if stack[-1] == "C" and val == "D":
                    stack.pop()
                    continue
            stack.append(val)
        return len(stack)
