class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1     
        row_index = -1     
        
        for i in range(len(mat)):
            count_ones = 0   
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count_ones += 1  
            
            if count_ones > max_ones:
                max_ones = count_ones
                row_index = i   
        
        return [row_index, max_ones]
