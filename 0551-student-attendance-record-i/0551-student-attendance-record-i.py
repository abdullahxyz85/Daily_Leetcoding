class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2:
            return False  # not eligible

        # Condition 2: check if student was late 3 or more consecutive days
        if 'LLL' in s:
            return False  # not eligible

        # If both conditions are fine, eligible
        return True

