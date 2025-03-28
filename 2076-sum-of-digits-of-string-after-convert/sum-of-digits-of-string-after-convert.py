class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet_values = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 
            'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 
            'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
        }

        num_str = ""
        for ch in s:
            num_str += str(alphabet_values[ch])

        while k > 0:
            sum_digits = 0
            for digit in num_str:
                sum_digits += int(digit)
            num_str = str(sum_digits)
            k -= 1

        return int(num_str)