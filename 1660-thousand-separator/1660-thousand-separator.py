class Solution:
    def thousandSeparator(self, n: int) -> str:
        # if number is less than 1000, just return it as string
        if n < 1000:
            return str(n)
        else:
            s = str(n)          # convert number to string
            length = len(s)     # total number of digits
            
            result = ""         # final string
            count = 0           # to count digits from right side
            
            # we will go from the last digit using index
            i = length - 1
            while i >= 0:
                result = s[i] + result   # add digit to the start of result
                count += 1               # increase count
                
                # if 3 digits passed and not at the start, add '.'
                if count % 3 == 0 and i != 0:
                    result = '.' + result
                
                i -= 1   
            
            return result
