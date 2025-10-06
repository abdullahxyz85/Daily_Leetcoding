class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool: 
        sorted_arr = sorted(arr)  
        difference = sorted_arr[1] - sorted_arr[0]

        for i in range(2, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i - 1] != difference:
                return False 
        return True  
