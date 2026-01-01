class Solution(object):
    def backspaceCompare(self, s, t):
        def process_string(text):
            result = []

            for ch in text:
                if ch != '#':
                    result.append(ch)
                else:
                    if result:
                        result.pop()

            return "".join(result)

        return process_string(s) == process_string(t)

        