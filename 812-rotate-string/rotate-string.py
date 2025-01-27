class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Step 1: Check if lengths match
        if len(s) != len(goal):
            return False

        # Step 2: Generate all rotations of s
        n = len(s)
        for i in range(n):
            # Perform a left rotation
            s = s[1:] + s[0]  # Move first character to the end
            # Compare with goal
            if s == goal:
                return True
        
        # If no rotation matches, return False
        return False

