class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # First, check if the lengths are not equal
        if len(s) != len(goal):
            return False
        
        # If s and goal are already equal, check for duplicate characters
        if s == goal:
            char_count = {}
            for char in s:
                if char in char_count:
                    return True  # If a character repeats, we can swap the same characters
                char_count[char] = 1
            return False  # If all characters are unique, we cannot swap

        # Find indices where s and goal differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # If there are exactly 2 differences, check if swapping makes them equal
        if len(diff) == 2:
            i, j = diff[0], diff[1]
            return s[i] == goal[j] and s[j] == goal[i]
        
        return False  # If there are more or less than 2 differences, swapping won't help
