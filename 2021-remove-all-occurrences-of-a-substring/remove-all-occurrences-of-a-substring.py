class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:  # Keep removing until 'part' is no longer in 's'
            s = s.replace(part, "", 1)  # Remove only the leftmost occurrence
        return s
