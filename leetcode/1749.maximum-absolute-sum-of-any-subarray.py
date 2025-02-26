#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

from typing import List
# @lc code=start


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        champ = 0
        curr = 0
        sign = nums[0] < 0

        for n in nums:
            if n == 0:
                continue

            if (n < 0) != sign:
                champ = max(champ, curr)
                curr = 0
                sign = n < 0

            curr += abs(n)

        return champ

# @lc code=end
