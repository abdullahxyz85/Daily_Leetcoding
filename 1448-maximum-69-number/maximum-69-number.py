class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = list(str(num))  # Convert number to list of characters for easy modification
        for i in range(len(num_str)):
            if num_str[i] == '6':  # Find the first '6'
                num_str[i] = '9'  # Change it to '9'
                break  # Stop after the first change
        return int("".join(num_str))  # Convert back to integer and return