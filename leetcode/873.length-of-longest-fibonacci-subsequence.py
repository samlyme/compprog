#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

import enum
from typing import List
# @lc code=start


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: idx for idx, num in enumerate(arr)}
        # MUST BE 2D
        memo = {}   # Records the max length of a fib sequence with keys a, b
        max_length = 0

        # We need to do this "right to left", since values to the left depend
        # on values from the right
        # a + b = c
        for b in range(len(arr) - 2, 0, -1):
            for c in range(b + 1, len(arr)):
                a = index.get(arr[c] - arr[b], -1)
                if a != -1 and a < b:
                    memo[(a, b)] = max(
                        memo.get((b, c), 2) + 1, memo.get((a, b), 3))
                    max_length = max(max_length, memo[(a, b)])

        return max_length if max_length > 2 else 0
# @lc code=end
