class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  # If total candies are less than k children, return 0
            return 0
        
        low, high = 1, max(candies)
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2  # Possible candy count per child
            count = 0  # Count how many children can be served
            
            # Calculate the number of children we can serve
            for c in candies:
                count += c // mid  # How many children can get 'mid' candies from this pile
            
            if count >= k:  # If we can serve at least k children
                ans = mid  # Store the possible answer
                low = mid + 1  # Try for a bigger number
            else:
                high = mid - 1  # Try for a smaller number
                
        return ans