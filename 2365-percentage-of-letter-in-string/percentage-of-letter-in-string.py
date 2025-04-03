class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
            freq = {}
            for i in s:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
            
            letter_count = 0
            if letter in freq:
                letter_count = freq[letter]
            
            percentage = (letter_count / len(s)) * 100
            
            return int(percentage)