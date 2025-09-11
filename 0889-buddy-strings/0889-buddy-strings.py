class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            char_count = {}
            for char in s:
                if char in char_count:
                    return True 
                char_count[char] = 1
            return False  

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        if len(diff) == 2:
            i, j = diff[0], diff[1]
            return s[i] == goal[j] and s[j] == goal[i]
        
        return False  