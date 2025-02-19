#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dpl = cost[0]
        dpr = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(dpl, dpr)
            dpl = dpr
            dpr = cur

        return min(dpl, dpr)

# @lc code=end
