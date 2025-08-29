class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            new_word = word[:i] + word[i+1:]
            
            freq = {}
            for ch in new_word:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
            
            values = list(freq.values())
            
            if len(set(values)) == 1:
                return True
        
        return False
