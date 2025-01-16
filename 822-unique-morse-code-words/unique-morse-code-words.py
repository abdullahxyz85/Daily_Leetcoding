class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", 
            ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", 
            ".--", "-..-", "-.--", "--.."
        ]
        
        transformations = []
        
        for word in words:
            transformation = ""
            for char in word:
                index = 0
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if char == letter:
                        break
                    index += 1
                transformation += morse_code[index]
            if transformation not in transformations:
                transformations.append(transformation)
        
        return len(transformations)


