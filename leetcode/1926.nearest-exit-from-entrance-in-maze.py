#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        depth = 1
        frontier = deque([(entrance[0], entrance[1])])
        explored = set()
        
        while frontier:
            for _ in range(len(frontier)):
                curr = frontier.popleft()

                for dir in DIRECTIONS:
                    n = tuple(a + b for a, b in zip(curr, dir))
                    if 
                

            depth += 1
        return -1
# @lc code=end

