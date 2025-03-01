#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

from typing import List
# @lc code=start


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i+1] = 0

        # shift zeros
        j = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[k], nums[j] = nums[j], nums[k]
                j += 1

        return nums
# @lc code=end
