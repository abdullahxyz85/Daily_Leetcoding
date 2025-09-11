class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [0] * n   # this will store the result for each index

        # Step 1: Left-to-right pass
        prev = float('-inf')  # start with negative infinity (means we haven't seen c yet)
        for i in range(n):
            if s[i] == c:
                prev = i
            answer[i] = i - prev   # distance from the nearest c on the left

        # Step 2: Right-to-left pass
        prev = float('inf')  # reset to positive infinity
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            # take the minimum distance from left pass and right pass
            answer[i] = min(answer[i], prev - i)

        return answer
