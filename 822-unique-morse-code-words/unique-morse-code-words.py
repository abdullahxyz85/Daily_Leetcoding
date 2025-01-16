class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a = "abcdefghijklmnopqrstuvwxyz"
        p = []
        ans = []
        for q in words:
            b = ""
            for i in q:
                b += m[a.index(i)]
            p.append(b)
        for q in p:
            if q not in ans:
                ans.append(q)
        return len(ans)


