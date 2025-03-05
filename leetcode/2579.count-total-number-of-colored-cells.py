#
# @lc app=leetcode id=2579 lang=python3
#
# [2579] Count Total Number of Colored Cells
#

# @lc code=start
class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1

        return 4 * (n-1) + self.coloredCells(n-1)

# @lc code=end
