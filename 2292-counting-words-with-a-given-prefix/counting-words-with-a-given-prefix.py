class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
            count = 0
            pref_length = len(pref)
            for word in words:
                if word[:pref_length] == pref:
                  count +=1
            return count
        
        
        
        # count = 0
        # for word in words:
        #     if word.startswith(pref):
        #         count +=1
        # return count