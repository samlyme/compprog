#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from collections import deque


class Solution:
    letters = {
        "2": list("abc"),
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz")
    }
    def letterCombinations(self, digits: str) -> List[str]: # type: ignore
        if len(digits) == 0: return list()
        
        words = deque(self.letters[digits[0]])

        for d in digits[1:]:
            for _ in range(len(words)):
                word = words.popleft()
                for l in self.letters[d]:
                    words.append(word + l)

        return list(words)
        
# @lc code=end

