class Solution:
    def digitSum(self, s: str, k: int) -> str:
            while len(s) > k:
                new_s = ""
                i = 0
                while i < len(s):
                    chunk_sum = 0
                    j = 0
                    while j < k and i + j < len(s):  # Ensure we don't go out of bounds
                        chunk_sum += int(s[i + j])   # Convert character to integer and sum
                        j += 1
                    new_s += str(chunk_sum)  # Convert sum back to string and append
                    i += k  # Move to the next chunk
                s = new_s  # Update s with the new transformed string
            return s