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
            # explored[start] = True

            while frontier:
                curr, depth = frontier.pop()
                path[depth] = curr

                for successor in graph[curr]:
                    if not safe[successor] or successor in path[:depth+1]:
                        safe[successor] = False
                        for i in range(depth+1):
                            safe[path[i]] = False
                        depth = -1
                    if not explored[successor]:
                        frontier.append((successor, depth+1))
                        explored[successor] = True

        return [state for state, is_safe in enumerate(safe) if is_safe]

# @lc code=end
