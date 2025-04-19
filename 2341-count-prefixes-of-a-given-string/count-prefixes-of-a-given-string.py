class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0

        for word in words:
            is_prefix = True
            
            # If word is longer than s, it can't be a prefix
            if len(word) > len(s):
                continue
            
            for i in range(len(word)):
                if word[i] != s[i]:
                    is_prefix = False
                    break
            
            if is_prefix:
                count += 1
        
        return count