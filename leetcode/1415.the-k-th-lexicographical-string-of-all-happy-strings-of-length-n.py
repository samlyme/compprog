#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
from typing import Iterator


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphabet = ["a", "b", "c"]

        def happyStrings(n: int, prev: str) -> Iterator[str]:
            if n == 0:
                yield ""
                return

            for char in alphabet:
                if char == prev:
                    continue
                for string in happyStrings(n-1, char):
                    yield char + string

        strings = happyStrings(n, "")
        try:
            while k > 1:
                print(next(strings))
                k -= 1
            return next(strings)
        except:
            return ""

# @lc code=end
