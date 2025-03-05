#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#
from collections import deque
from typing import List
# @lc code=start


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # idea is to do a dfs, while tracking the path it took in a
        # separate data structure. If you reach a loop, all nodes in that
        # path are unsafe.

        path = [-1] * len(graph)
        frontier = []
        safe = [True] * len(graph)
        explored = [False] * len(graph)

        for start in range(len(graph)):
            frontier.append((start, 0))

            while frontier:
                curr, depth = frontier.pop()
                path[depth] = curr
                if not safe[curr] or curr in path[:depth]:
                    safe[curr] = False
                    for i in range(depth):
                        safe[path[i]] = False
                    depth = -1

                if not explored[curr]:
                    for successor in graph[curr]:
                        frontier.append((successor, depth+1))

                explored[curr] = True

        return [state for state, is_safe in enumerate(safe) if is_safe]

# @lc code=end
