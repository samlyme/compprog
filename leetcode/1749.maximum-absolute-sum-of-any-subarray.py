#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

from typing import List
# @lc code=start


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        curr_max = 0
        curr_min = 0
        for x in nums:
            curr_max = max(x, curr_max + x)
            curr_min = min(x, curr_min + x)
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, abs(min_sum))

# @lc code=end
