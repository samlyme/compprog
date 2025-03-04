#
# @lc app=leetcode id=1765 lang=python3
#
# [1765] Map of Highest Peak
#

from collections import deque
from typing import List
# @lc code=start


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        frontier = deque()
        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    isWater[row][col] = 0
                    frontier.append((row, col))
                else:
                    isWater[row][col] = -1

        while frontier:
            px, py = frontier.popleft()

            for dx, dy in dirs:
                nx, ny = px + dx, py + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if isWater[nx][ny] == -1:
                        frontier.append((nx, ny))
                        isWater[nx][ny] = isWater[px][py] + 1

        return isWater

# @lc code=end
