class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter

        # Count character frequencies
        freq = Counter(s)
        
        # Count the number of characters with odd frequencies
        odd_count = sum(1 for count in freq.values() if count % 2 != 0)
        
        # Check if the conditions are satisfied
        return odd_count <= k <= len(s)