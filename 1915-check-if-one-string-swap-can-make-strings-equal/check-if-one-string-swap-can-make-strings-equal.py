class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:  # If both strings are already equal, return True
            return True

        diff_count = 0  # Count of different characters
        first_index = -1
        second_index = -1

        for i in range(len(s1)):  # Loop through each character
            if s1[i] != s2[i]:  # If characters at the same position are different
                diff_count += 1  # Increase difference count
                
                if diff_count == 1:
                    first_index = i  # Store first mismatch position
                elif diff_count == 2:
                    second_index = i  # Store second mismatch position
                else:
                    return False  # If there are more than 2 mismatches, return False

        # Check if swapping makes them equal
        if diff_count == 2 and s1[first_index] == s2[second_index] and s1[second_index] == s2[first_index]:
            return True
        
        return False  # Otherwise, return False
