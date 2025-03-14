class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total_sum = 0

        for i in range(n):
            total_subarrays = (i + 1) * (n - i)
            
            odd_contribution = (total_subarrays + 1) // 2  # Ceiling division for odd-length subarrays
            
            # Add to total sum
            total_sum += arr[i] * odd_contribution
        
        return total_sum