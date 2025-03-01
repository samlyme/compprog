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
        for i in range(len(nums) - 1):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) - 1 and nums[j] == 0:
                    j += 1
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
# @lc code=end
