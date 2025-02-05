#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
from collections import deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = [set() for _ in range(n)]
        inv_list = [set() for _ in range(n)]
       
        for init, term in connections:
            adj_list[init].add(term)
            inv_list[term].add(init)

        # is a tree with root zero
        # if you can reach a node from zero, then you must reorder the path
        count = 0
        frontier = deque([0])
        visited = [False] * n

        while frontier:
            curr = frontier.pop()
            visited[curr] = True
            
            for next in adj_list[curr]:
                if not visited[next]:
                    count += 1
                    frontier.append(next)

            for next in inv_list[curr]:
                if not visited[next]:
                    frontier.append(next)

        return count
        
        
# @lc code=end

