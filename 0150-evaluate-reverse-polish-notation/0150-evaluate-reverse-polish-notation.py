
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:   #tokens = ["2","1","+","3","*"]
            if token in ['+','-','*','/']:
                b = stack.pop()   # a will come first and b last
                a = stack.pop()   # Here the sequence of a and b is important
                
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(a / b)
                stack.append(res)
                
            else:
                stack.append(int(token))

        return stack[0]
