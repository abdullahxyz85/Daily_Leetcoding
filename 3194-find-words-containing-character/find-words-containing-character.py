from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if x in words[i]:  # check if x is in the current word
                result.append(i)  # append the index of the word
        return result
