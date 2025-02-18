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
        m = len(maze)
        n = len(maze[0])
        if m == 1 and n == 1:
            return -1

        depth = 0
        queue = deque([(entrance[0], entrance[1])])  # step 1
        maze[entrance[0]][entrance[1]] = "+"  # step 2

        while queue:

            for _ in range(len(queue)):
                row, col = queue.popleft()  # step 3
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # step 4
                    nr, nc = row + dy, col + dx
                    # step 5
                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                        if (nr == 0 or nr == m - 1) or (nc == 0 or nc == n - 1):
                            return depth + 1

                        maze[nr][nc] = "+"
                        queue.append((nr, nc))

            depth += 1

        return -1

    def isExit(self, maze: List[List[str]], coord: tuple[int, int]) -> bool:
        if maze[coord[0]][coord[1]] == "+":
            return False

        return (coord[0] == 0 or coord[0] == len(maze) - 1
                or coord[1] == 0 or coord[1] == len(maze[0]) - 1)
# @lc code=end
