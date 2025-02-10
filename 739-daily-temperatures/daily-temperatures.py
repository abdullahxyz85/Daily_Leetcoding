class Solution:
    def dailyTemperatures(self,T: List[int]) -> List[int]:
        s = []
        r = [0] * len(T)

        for i in range (len(T)):
            while s and T[i] > T[s[-1]]:
                index = s.pop()
                r[index] = i - index
            s.append(i)
        
        return r