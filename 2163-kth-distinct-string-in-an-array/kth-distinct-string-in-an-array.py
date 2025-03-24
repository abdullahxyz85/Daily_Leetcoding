class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for word in arr:
            if word in freq:  
                freq[word] += 1
            else: 
                freq[word] = 1

        distinct_strings = []
        for word in arr:
            if freq[word] == 1:  
                distinct_strings.append(word)

        if k <= len(distinct_strings):
            return distinct_strings[k - 1]  
        return ""  
