class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  
            return 0
        
        low, high = 1, max(candies) 
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2  
            count = 0  
            
            for c in candies:
                count += c // mid  
            
            if count >= k:  
                ans = mid  
                low = mid + 1  
            else:
                high = mid - 1  
                
        return ans