class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
            freq = {}
            for i in s:                                                                       # s = "foobar", letter = "d"
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
            
            if letter in freq:
                letter_count = freq[letter] # freq["o"]
            else:
                letter_count = 0
            
            percentage = (letter_count / len(s)) * 100
            
            return int(percentage)