#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#

from typing import List
# @lc code=start


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        out = []

        a, b = 0, 0

        while a < len(nums1) and b < len(nums2):
            id1, val1 = nums1[a]
            id2, val2 = nums2[b]

            if id1 < id2:
                out.append([id1, val1])
                a += 1
            elif id1 > id2:
                out.append([id2, val2])
                b += 1
            else:
                out.append([id1, val1 + val2])
                a += 1
                b += 1

        if a < len(nums1):
            out.extend(nums1[a:])
        elif b < len(nums2):
            out.extend(nums2[b:])

        return out
# @lc code=end
