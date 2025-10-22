class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_right = -1  
        
        for i in range(len(arr) - 1, -1, -1):
            current_value = arr[i]   
            arr[i] = max_right       
            if current_value > max_right:
                max_right = current_value  
        
        return arr  
