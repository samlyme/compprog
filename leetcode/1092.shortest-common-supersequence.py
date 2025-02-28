#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = (1 + dp[i-1][j-1]
                            if str1[i - 1] == str2[j-1]
                            else max(dp[i][j-1], dp[i-1][j]))

        i, j = n, m
        out = []

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                # If the characters are the same, add it once
                out.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                # If coming from top has higher value, take character from str1
                out.append(str1[i-1])
                i -= 1
            else:
                # Otherwise, take character from str2
                out.append(str2[j-1])
                j -= 1

        # Add remaining characters from str1 (if any)
        while i > 0:
            out.append(str1[i-1])
            i -= 1

        # Add remaining characters from str2 (if any)
        while j > 0:
            out.append(str2[j-1])
            j -= 1

        # Reverse the result to get the final supersequence
        return ''.join(out[::-1])


# @lc code=end
