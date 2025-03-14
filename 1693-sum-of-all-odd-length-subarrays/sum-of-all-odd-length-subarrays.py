class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        # Loop through every starting index
        for i in range(n):
            # Loop through every possible odd-length subarray
            for j in range(i, n, 2):  # Step of 2 ensures odd-length
                total_sum += sum(arr[i:j+1])  # Sum the subarray and add to total sum
        
        return total_sum