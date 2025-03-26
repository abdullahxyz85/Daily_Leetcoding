class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)  #word = "abcdefd", ch = "d" Output: "dcbaefd"  ["a", "b", "c", "d", "e", "f", "h"]
        
        index = -1
        for i in range(len(word_list)):
            if word_list[i] == ch: 
                index = i
                break
        
        if index == -1:
            return word
        
        left, right = 0, index
        while left < right:
            word_list[left], word_list[right] = word_list[right], word_list[left]
            left += 1
            right -= 1
        
        return "".join(word_list)
