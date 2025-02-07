#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0: return False
        if n == 1: return True

        bits = bin(n)[2:]
        
        if bits.count('1') > 1: return False
        count = 0
        for b in reversed(bits):
            if b == '0': 
                count += 1
            else: break
        return count > 0 and count % 2 == 0
# @lc code=end

