class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        odd_Num = []
        even_Num = []

        # Count the frequency of each character
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Separate frequencies into odd and even lists
        for count in freq.values():
            if count % 2 == 0:
                even_Num.append(count)
            else:
                odd_Num.append(count)

        # If there is no odd or even frequency, return -1
        if not odd_Num or not even_Num:
            return -1

        # Initialize max_diff to a very small number
        max_diff = -1000  # You can use any small number here

        # Loop through all odd and even frequencies
        for odd in odd_Num:
            for even in even_Num:
                diff = odd - even  # Calculate the difference
                if diff > max_diff:
                    max_diff = diff  # Update if we find a bigger difference

        return max_diff
