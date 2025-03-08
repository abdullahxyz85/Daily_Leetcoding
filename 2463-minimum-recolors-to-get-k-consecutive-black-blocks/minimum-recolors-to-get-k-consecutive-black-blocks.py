class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = blocks[:k].count('W')
        current_white_count = min_operations
        
        # Sliding window approach
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':  # Remove leftmost character of previous window
                current_white_count -= 1
            if blocks[i] == 'W':  # Add new character to current window
                current_white_count += 1
            
            # Update the minimum operations needed
            min_operations = min(min_operations, current_white_count)
        
        return min_operations