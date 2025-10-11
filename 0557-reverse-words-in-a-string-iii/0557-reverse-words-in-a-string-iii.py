class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()   

        reversed_words = []

        for char in s_split:
            list_char = list(char)  

            list_char.reverse()     

            reversed_word = ''.join(list_char)  

            reversed_words.append(reversed_word)

        return ' '.join(reversed_words)
