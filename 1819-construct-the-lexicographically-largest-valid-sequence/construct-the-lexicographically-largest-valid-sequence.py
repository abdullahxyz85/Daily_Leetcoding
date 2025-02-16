from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        seq = [0] * (2 * n - 1)  # Initialize sequence with zeros
        used = set()  # Track used numbers
        
        def backtrack(index: int) -> bool:
            if index == len(seq):  # Base case: fully filled sequence
                return True
            
            if seq[index] != 0:  # Skip filled positions
                return backtrack(index + 1)
            
            for num in range(n, 1, -1):  # Try placing numbers from n to 2
                if num in used:
                    continue
                if index + num < len(seq) and seq[index + num] == 0:
                    # Place num at index and index + num
                    seq[index], seq[index + num] = num, num
                    used.add(num)
                    
                    if backtrack(index + 1):
                        return True
                    
                    # Backtrack
                    seq[index], seq[index + num] = 0, 0
                    used.remove(num)
            
            # Place 1 (since it appears only once)
            if 1 not in used:
                seq[index] = 1
                used.add(1)
                
                if backtrack(index + 1):
                    return True
                
                # Backtrack
                seq[index] = 0
                used.remove(1)
            
            return False
        
        backtrack(0)
        return seq
