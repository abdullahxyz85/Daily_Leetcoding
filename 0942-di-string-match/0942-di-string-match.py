class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        
        low = 0
        high = n
        
        result = []
        
        for ch in s:
            if ch == 'I':
                result.append(low)
                low += 1
            else:  
                result.append(high)
                high -= 1
        
        result.append(low)  
        
        return result