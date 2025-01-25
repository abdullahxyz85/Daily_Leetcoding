class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for char in s:
            if char == 'i':
                result.reverse()  # Reverse the list when 'i' is encountered
            else:
                result.append(char)  # Append character to the list
        return ''.join(result)  # Join the list to form the final string
