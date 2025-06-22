class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_lines = 1         
        current_line_width = 0    

        for letter in s:
            index = ord(letter) - ord('a')  
            letter_width = widths[index]

            if current_line_width + letter_width > 100:
                total_lines += 1               
                current_line_width = letter_width  
            else:
                current_line_width += letter_width  

        return [total_lines, current_line_width]