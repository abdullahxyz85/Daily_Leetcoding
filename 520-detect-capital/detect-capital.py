class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        # Case 1: All characters are uppercase
        all_capital = True
        for i in range(n):
            if 'A' <= word[i] <= 'Z':  # Checking if uppercase
                continue
            all_capital = False
            break

        # Case 2: All characters are lowercase
        all_lower = True
        for i in range(n):
            if 'a' <= word[i] <= 'z':  # Checking if lowercase
                continue
            all_lower = False
            break

        # Case 3: Only the first letter is uppercase and the rest are lowercase
        first_capital_rest_lower = True
        if not ('A' <= word[0] <= 'Z'):  # First letter should be uppercase
            first_capital_rest_lower = False
        for i in range(1, n):
            if not ('a' <= word[i] <= 'z'):  # Remaining should be lowercase
                first_capital_rest_lower = False
                break

        # Return True if any of the three conditions hold
        return all_capital or all_lower or first_capital_rest_lower

