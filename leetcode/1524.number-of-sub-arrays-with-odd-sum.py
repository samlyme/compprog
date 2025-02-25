#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = odd = even = 0
        for x in arr:
            even += 1
            if x % 2:
                odd, even = even, odd
            res = (res + odd) % 1000000007
        return res
# @lc code=end
