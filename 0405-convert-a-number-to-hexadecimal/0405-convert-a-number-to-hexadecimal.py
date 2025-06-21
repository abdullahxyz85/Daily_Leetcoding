class Solution:
    def toHex(self, num: int) -> str:
        hex_map = "0123456789abcdef"
        
        if num == 0:
            return "0"
        
        if num < 0:
            num += 2 ** 32  
        
        hex_str = ""
        
        while num > 0:
            remainder = num % 16
            hex_char = hex_map[remainder]
            hex_str = hex_char + hex_str 
            num = num // 16  
        
        return hex_str
