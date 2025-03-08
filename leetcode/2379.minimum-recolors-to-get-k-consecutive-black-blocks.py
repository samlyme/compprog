#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0  # current no. of white in window

        for j in range(k):
            if blocks[j] == 'W':
                w += 1

        out = w

        for i in range(1, len(blocks) - k + 1):
            j = i + k - 1
            if blocks[i-1] == 'W':
                w -= 1
            if blocks[j] == 'W':
                w += 1
            out = min(out, w)

        return out


# @lc code=end
