class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            for j in range(i, n, 2):  
                total_sum += sum(arr[i:j+1])  
        
        return total_sum