#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
from typing import List


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def rev(list: List, a: int, b: int) -> None:
            while a < b:
                list[a], list[b] = list[b], list[a]
                a += 1
                b -= 1

        low = 1
        dec_start = -1
        vals = [0] * (len(pattern) + 1)
        vals[0] = 1

        for idx, c in enumerate(pattern):
            low += 1
            vals[idx+1] = low
            if dec_start == -1:
                if c == 'D':
                    dec_start = idx
            else:
                if c == 'I':
                    rev(vals, dec_start, idx)
                    dec_start = -1

        if pattern[-1] == 'D':
            rev(vals, dec_start, len(pattern))

        out = 0
        for val in vals:
            out = out * 10 + val
        return str(out)
        # @lc code=end
