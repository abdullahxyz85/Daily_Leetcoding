class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0

        for sentence in sentences:
            space_count = 0
            for char in sentence:
                if char == " ":
                    space_count += 1
            word_count = space_count + 1
            max_words = max(max_words,word_count)
        return max_words


