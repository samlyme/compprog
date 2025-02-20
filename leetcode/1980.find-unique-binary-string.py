#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join(['1' if num[i] == '0' else '0' for i, num in enumerate(nums)])
        # @lc code=end
