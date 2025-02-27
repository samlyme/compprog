#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

from typing import List
# @lc code=start


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # some type of dp problem, where you can choose to include
        # the current item or not.
        # if a choice does not satisfy the fib, return 0
        # each "recursion" only needs to look back 2 items
        # each "recursion" has a simple condition to end,
        #   using binary search
        def binary_search(target: int, l: int, r: int) -> int:
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        # max length for a given a, b
        memo = [[-1] * len(arr) for _ in range(len(arr))]

        # given a, b, search if the rest has a valid "c"
        def rec(a: int, b: int) -> int:
            if memo[a][b] != -1:
                return memo[a][b]

            c = binary_search(arr[a]+arr[b], b+1, len(arr) - 1)
            # print(a, b, c)
            if c == -1:  # valid c does not exist
                memo[a][b] = 0
                return 0

            memo[a][b] = 1 + rec(b, c)
            # if memo[a][b] == 4:
            #     print(a, b, c)
            return memo[a][b]

        out = max([rec(a, b)
                   for a in range(len(arr)-2)
                   for b in range(a + 1, len(arr) - 1)])

        # for row in memo:
        #     print(row)
        return 0 if out == 0 else 2 + out
# @lc code=end
