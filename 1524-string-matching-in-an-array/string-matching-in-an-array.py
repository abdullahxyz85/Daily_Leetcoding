class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        
        for word in words:
            for other in words:
                if word != other and word in other:  
                    result.append(word)
                    break  
        
        return result  