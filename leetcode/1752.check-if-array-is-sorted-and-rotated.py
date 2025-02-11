#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool: # type: ignore
        min_idx = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < prev:
                min_idx = i
                break
            prev = curr

        prev = nums[min_idx]
        for i in range(1, len(nums)):
            curr = nums[(i+min_idx) % len(nums)]
            if curr < prev:
                return False
            prev = curr
        return True
        
# @lc code=end

