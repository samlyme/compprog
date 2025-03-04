#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# @lc code=start


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # generate a list of powers of 3 less than n
        powers = []
        p = 1
        while p <= n:
            powers.append(p)
            p *= 3

        def rec(n: int, prevs: tuple[int, ...]):
            if n == 0:
                return True

            if not prevs:
                for i in range(len(powers)):
                    if rec(n-powers[i], (i,)):
                        return True
                return False
            else:
                for i in range(prevs[-1] + 1, len(powers)):
                    if rec(n-powers[i], prevs + (i,)):
                        return True
                return False
        return rec(n, ())

# @lc code=end
