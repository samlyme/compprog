#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums.sort()
        if int(nums[0], 2) != 0:
            return '0' * n

        if int(nums[-1], 2) < 2 ** n - 1:
            return str(bin(2 ** n - 1))[2:].rjust(n, '0')

        for i in range(len(nums) - 1):
            a = int(nums[i], 2)
            b = int(nums[i+1], 2)
            if b - a > 1:
                return str(bin(a+1))[2:].rjust(n, '0')

        return ""
        # @lc code=end
