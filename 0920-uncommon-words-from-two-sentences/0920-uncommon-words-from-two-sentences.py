class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1 = s1.split() # ["this", "apple", "is", "sweet"]
        w2 = s2.split() # ["this", "apple", "is", "sour"]
        
        all_w = w1 + w2  #["this", "apple", "is", "sweet", "this", "apple", "is", "sour"]
        
        count = {}   # {"this": 2, "apple": 2, "is": 2, "sweet" : 1, "sour": 1}
        for w in all_w:
            if w in count:
                count[w] += 1 
            else:
                count[w] = 1
        
        res = []
        for w in count:
            if count[w] == 1:
                res.append(w)
        
        return res