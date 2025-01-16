class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
            ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
            ".--", "-..-", "-.--", "--.."
        ]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        morse_words = []  
        unique_morse = [] 
        
        for word in words:
            morse_representation = "" 
            for char in word:
                morse_representation += morse_code[alphabet.index(char)]  
            morse_words.append(morse_representation)  
        
        for morse_word in morse_words:
            if morse_word not in unique_morse: 
                unique_morse.append(morse_word)
        
        return len(unique_morse) 



