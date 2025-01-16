class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
            ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
            ".--", "-..-", "-.--", "--.."
        ]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        morse_words = []  # List to store Morse code translations of words
        unique_morse = []  # List to store unique Morse code representations
        
        for word in words:
            morse_representation = ""  # To build the Morse code for the current word
            for char in word:
                morse_representation += morse_code[alphabet.index(char)]  # Convert char to Morse
            morse_words.append(morse_representation)  # Add Morse code of the word to the list
        
        for morse_word in morse_words:
            if morse_word not in unique_morse:  # Check if it's a unique representation
                unique_morse.append(morse_word)
        
        return len(unique_morse)  # Return the count of unique representations



