class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Step 1: Compute LCS using DP
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

        lcs = dp[m][n]  # Get the longest common subsequence

        # Step 2: Construct SCS using LCS
        i, j, k = 0, 0, 0
        result = []

        for c in lcs:
            while i < len(str1) and str1[i] != c:
                result.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                result.append(str2[j])
                j += 1
            
            # Append LCS character
            result.append(c)
            i += 1
            j += 1

        # Append remaining characters of str1 and str2
        result.append(str1[i:])
        result.append(str2[j:])

        return "".join(result)
