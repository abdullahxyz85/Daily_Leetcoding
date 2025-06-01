class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        freq1 = {}
        freq2 = {}
        for i in words1:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1
        for i in words2:
            if i in freq2:
                freq2[i] += 1
            else:
                freq2[i] = 1
        for i in freq1:
            if freq1[i] == 1 and i in freq2 and freq2[i] == 1:
                count += 1
        return count